"use strict";

import { sanitize } from "@strapi/utils";

const sanitizeContent = async (context, data, contentType) => {
  return sanitize.contentAPI.output(data, contentType, {
    auth: context.state.auth,
  });
};

export default {
  async applicationAnalysis(context) {
    try {
      const { data } = context.request.body;
      const { application, aiMessages } = data;

      const contentType = strapi.contentType("api::application.application");

      const analysedApplication = await strapi
        .service("api::gia.gia")
        .applicationAnalysis(application, aiMessages);

      if (!!analysedApplication?.id) {
        const sanitizedApplication = await sanitizeContent(
          context,
          analysedApplication,
          contentType
        );

        context.response.status = 200;
        context.response.body = sanitizedApplication;
      } else {
        context.response.status = 500;
        context.response.body = {
          error: "Something went wrong with the server.",
        };
      }
    } catch (error) {
      context.response.status = 500;

      context.response.body = { error: error?.message };
    }
  },
};
