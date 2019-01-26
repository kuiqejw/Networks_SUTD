import Vue from 'vue';
import Vuex from 'vuex';

// eslint-disable-next-line import/no-unresolved
import { isDevelopment } from 'common/util';
import query from './modules/query';
import status from './modules/status';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    query,
    status,
  },
  strict: isDevelopment,
});
