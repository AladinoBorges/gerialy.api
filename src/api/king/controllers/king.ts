"use strict";

export default {
  async kong(context) {
    context.response.status = 200;
    context.response.body = { kong: "donkey, 1981. a2600" };
  },
};
