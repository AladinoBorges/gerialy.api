import { sanitize } from "@strapi/utils";
import { Context } from "koa";

const sanitizeContent = async (context, data, contentType) => {
  return sanitize.contentAPI.output(data, contentType, {
    auth: context.state.auth,
  });
};

export default {
  async applicationAnalysis(context: Context) {
    const { application, aiMessages } = context.body as {
      application: string;
      aiMessages: string;
    };

    const contentType = strapi.contentType("api::application.application");

    const analysedApplication = await strapi
      .service("api::gia.gia")
      .applicationAnalysis(application, aiMessages);

    if (!!analysedApplication?.id) {
      const sanitizedApplication = await sanitizeContent(
        analysedApplication,
        context,
        contentType
      );

      context.status = 200;
      context.body = sanitizedApplication;
    } else {
      context.status = 500;
      context.body = { error: "Something went wrong with the server." };
    }
  },
};
