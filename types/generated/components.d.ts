import type { Schema, Attribute } from '@strapi/strapi';

export interface RecruitmentStages extends Schema.Component {
  collectionName: 'components_recruitment_stages';
  info: {
    displayName: 'stages';
    icon: 'check';
  };
  attributes: {
    name: Attribute.String &
      Attribute.Required &
      Attribute.SetMinMaxLength<{
        minLength: 1;
        maxLength: 100;
      }>;
  };
}

export interface RecruitmentProcess extends Schema.Component {
  collectionName: 'components_recruitment_processes';
  info: {
    displayName: 'process';
    icon: 'bulletList';
  };
  attributes: {
    stage: Attribute.String &
      Attribute.SetMinMaxLength<{
        minLength: 1;
        maxLength: 100;
      }>;
    status: Attribute.Enumeration<['approved', 'disapproved', 'onHold']>;
  };
}

declare module '@strapi/types' {
  export module Shared {
    export interface Components {
      'recruitment.stages': RecruitmentStages;
      'recruitment.process': RecruitmentProcess;
    }
  }
}
