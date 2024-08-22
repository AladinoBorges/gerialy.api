import OpenAI from "openai";

const createNewEntry = async (contentType, data) => {
  const newEntry = await strapi.entityService.create(contentType.uid, {
    data,
  });

  return newEntry;
};

const updateEntry = async (contentType, id, data) => {
  const newEntry = await strapi.entityService.update(contentType.uid, id, {
    data,
  });

  return newEntry;
};

export default {
  async openAICompletion(messages) {
    const aiClient = new OpenAI();

    const newCompletion = await aiClient.chat.completions.create({
      model: "gpt-4o-mini",
      messages,
    });

    const contentCompletion =
      newCompletion.choices[0]?.message?.content?.trim();

    if (!!contentCompletion) {
      return JSON.parse(contentCompletion);
    }

    return null;
  },

  async applicationAnalysis(application, aiMessages) {
    const contentType = strapi.contentType("api::application.application");

    let newAIAnalysis = null;
    let analysedApplication = null;

    if (application?.id) {
      newAIAnalysis = await this.openAICompletion(aiMessages);
    }

    if (!!newAIAnalysis) {
      analysedApplication = await updateEntry(contentType, application?.id, {
        ...newAIAnalysis,
        analysedByIA: true,
        analysisDate: new Date(),
      });
    }

    return analysedApplication;
  },
};
