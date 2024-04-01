
import requests

url = "https://oec16-normal-useast5.us.tiktokv.com/api/v1/shop/product_info/get?iid=7344831596610357035&device_id=7344831037090678314&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=330804&version_name=33.8.4&device_platform=android&os=android&ab_version=33.8.4&ssmix=a&device_type=Nexus+4&device_brand=Google&language=en&os_api=28&os_version=9&openudid=fc60856675f2c7c&manifest_version_code=2023308040&resolution=768*1184&dpi=320&update_version_code=2023308040&_rticket=1710122532395&is_pad=0&current_region=US&app_type=normal&sys_region=US&last_install_time=1710101901&mcc_mnc=310260&timezone_name=America%2FNew_York&carrier_region_v2=310&residence=US&app_language=en&carrier_region=US&ac2=wifi&uoo=1&op_region=US&timezone_offset=-18000&build_number=33.8.4&host_abi=armeabi-v7a&locale=en&region=US&ts=1710122536&cdid=a2176f9b-badd-451a-a075-c2b56ed1737f"

headers = {
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Content-Length": "1271",
    "Content-Type": "application/json; charset=UTF-8",
      "Cookie": "store-idc=useast5; passport_csrf_token=dbc03c0d444d9a98b3dfaac97bb3a6c5; passport_csrf_token_default=dbc03c0d444d9a98b3dfaac97bb3a6c5; multi_sids=7344831583541920810%3Ac093bc17eb1da8e5ed571e03d5ff46f5; cmpl_token=AgQQAPNSF-RPsLXQ-86oJN0T_4-N2kqS_6jZYNF_tQ; odin_tt=9a050c4d8ad19c61854c17b4bc30fb8d31e509cd6d4c0f01dc1e634a6b65e8f9a0d5b8ec819c25be0def3441b4f37d217ccfab58ee3d94fcfc3da03e7b38523d638a8316e9f036a5415ce17141168899; sid_guard=c093bc17eb1da8e5ed571e03d5ff46f5%7C1710109523%7C5184000%7CThu%2C+09-May-2024+22%3A25%3A23+GMT; uid_tt=569bcaee9cd9457d68cee0f37d46753e6ef7233609a4844cd53264d620bf2c8d; uid_tt_ss=569bcaee9cd9457d68cee0f37d46753e6ef7233609a4844cd53264d620bf2c8d; sid_tt=c093bc17eb1da8e5ed571e03d5ff46f5; sessionid=c093bc17eb1da8e5ed571e03d5ff46f5; sessionid_ss=c093bc17eb1da8e5ed571e03d5ff46f5; store-country-code=us; store-country-code-src=uid; tt-target-idc=useast8; tt-target-idc-sign=fVIsWheYfD9FycwmIpV-pNZBwE2ZVdXZsfi5n4o98IlevySrZrEsA_puKnQG2nOh6zZqMSh255FW_R_wpYte0uOuTidxtdkmU-ajn9ovjXmNkHQK9fYucaFKJRxMT28QeaczrVBIhD19UYGmga7LtMiY3REQ0BzoBmKqaKtFjz7a5I1Q_AMqmp4NqkJtN8Bygmd2v10EYWj34Bn5v1FWJEwCHUUm2dp4f9u8E35f525Qp1zhBvYOJH-mLZIhUe2DnTZhSK7V-ua3CJiOn1Dg-iqtomykP2RjfZInGi8G0i-S0Cm1qLFL7PxsDHtZQtfR7AgF377mryTFgTWmpfeYSkNp4MDTpObSkM6QvhWojiQxPYV5p_BmoTsrr9E5fhsQLwndab4iHT07SdzhclOUM299FAIpIVI7SsGyzSNy2_sXuLA1eDmFIlEIeioV5f1HmiitgH_NVA9mKWgyi4Qr478Jfwz81S85CyLYubarODIg9pYBg57CS0Y40CdzxMNw; msToken=yI8so0AR7GBihObgad8ufy--vsgIJaUzuVgm7WysaHHtBwjvIdVAY6TZaXPAtDoLqz5duhvZ6QpLwF9SW3CjFFBFD6o1htaN_ITKb9X_pNqJSTx0Xla643v_kw==; user_oec_info=0a533d27d6b9b90afde42107a26dbb190a9e992491c89f78c38f8616ea609c7148ceff68489286ec1364c8244d56ff5fd8536731961e4643d0945fc601a1c5a01f02dd779949b80cff9c2db85d02accd148c3f829a1a490a3c20d043428fbaa7bcaee2514060807a1ae32e38b117ee91abe4fc29ffa61ec1d129711f0df797ece53038880c52445ed6aa658af7164d10f46523d7fb10cecfcb0d1886d2f6f20d220104bedbf22f",
      "Host": "oec16-normal-useast5.us.tiktokv.com",
      "passport-sdk-version": "5050090",
      "pns_event_id": "265",
      "sdk-version": "2",
      "User-Agent": "com.zhiliaoapp.musically/2023308040 (Linux; U; Android 9; en; Nexus 4; Build/PI;tt-ok/3.12.13.4-tiktok)",
      "X-Argus": "h5djlA5ECQUFQDkyzT7h03JXTPtgJG8ul0J24LXpFSAHgoYdM96aPV03iMX1sRAu6d5lQQ+lmkrLdJ+QXp0FMaktcvYD4p+Ap3UHWBkUqkUKthA4R0c9ikPRjFsOkgsvAs3UKBS2Z+V3lVbNbuedNORndp80YSujXzQXnHTCg2czZQ2k1NDEr0DTRyXIC66F4lKQW3C9zXVg2/oSTSmsIS+0DeXMSTyFslX2kJwBKKhndxerUC2D0pngGG9/zcL3ddzLo8QiYZxAhDSMujhyEkPeeZQgF5gwno1Zdnmcvy0Lft6w8z3N9Zi52qDt3BsfBAhJx0v+a/tJXzfNqdAItB47FYFqfs7mqFmPKG7efQWVG4uzjFru/A71RtrPswaanCdKhisH373htsJlacVIoL9LlAGPrziYFxa5H36SrP7HDIEtX5KCFF+wKD8T6VjOLIWfBCYVpZ3rI+5zo3W8EYCxsIuofbr+d54UB7W2+HiLlUShX75OyR70Rx8JotvOjHuQVHMn8I+mNw55R44l2SG6tqEREJ+nhIG/KERRy/JNMQ==",
      "X-Gorgon": "0404a09b40015ef419e3c206e9299c86c50d01f2a6194822a8fe",
      "X-Khronos": "1710122527",
      "X-Ladon": "qGR0OJO74UNHX4FQQku2x21vArfPPojhDdimASvXafexXeQ7",
      "X-SS-REQ-TICKET": "1710122532406",
      "X-SS-STUB": "FB5F7EDBF37299259FE00040CF562152",
    "x-tt-store-region": "us",
      "x-tt-store-region-src": "uid",
    "X-Tt-Token": "04c093bc17eb1da8e5ed571e03d5ff46f5042ce142c3d53196ae96ed58040c1eff42e4a27511b1a461942435b3d489e03afd3082a570ff1871bb494f31e654d554320fd0530f1af119f12f256d57b85918335653e9f15389ba113e3a4554e622eec38-CkA3NTc0NWNhZDYxYzZlZmI2ZGVjZjNiM2FkZTFkZmNhOTkxNzVhZjRkNDc2YTkxYmQ0NTFiZTAzY2MzYWM4YjEz-2.0.0",
      "x-vc-bdturing-sdk-version": "2.3.6.i18n"
}

data = {
      "template": "tt_pdp_full",
      "promotion_response_style": 1,
      "traffic_signature": "{\"scene\":\"PDPRecommend\"}",
      "product_source_info": {
          "1729438402051806054": 9
      },
      "biz_template": 3,
      "ship_to_addr": [],
      "request_scene": 1,
      "traffic_source_list": [
          6,
          9
      ],
      "experiment": {
          "param": {
              "ecom_logistic_display_opt": 1,
              "display_history_shipday": 1,
              "ecom_pdp_folding_display": 1,
              "is_new_pdp_logistic_module": 1,
              "is_new_pdp_sales_count_text": 1,
              "segregate_review_list": 0
          }
      },
    "product_id": [
        "1729438402051806054"
    ],
      "kol_id": "",
      "product_enter_context": {
          "1729438402051806054": {
              "req_type": 1
          }
      },
      "page_source_info": "{\"ec_head\":{\"extra\":{},\"page_name\":\"b2001\"},\"page_source_list\":[{\"extra\":{},\"page_name\":\"b2001\"},{\"extra\":{\"traffic_diversion_info\":\"{\\\"traffic_out_source\\\":\\\"homepage_top_2tab.in_app\\\",\\\"traffic_material_id\\\":\\\"\\\",\\\"traffic_campaign_id\\\":\\\"\\\",\\\"traffic_track_id\\\":\\\"1710122186525\\\",\\\"mall_btm\\\":\\\"a2270.b0865.c8949.d0\\\",\\\"mall_bcm\\\":\\\"|7312432294344589354|1||\\\"}\",\"prefix_ec_params_origin_is_mall_tab\":\"homepage_mall\",\"ec_next_page_c_btm_code\":\"c8949\"},\"page_name\":\"b0865\"},{\"extra\":{},\"page_name\":\"b0629\"},{\"extra\":{},\"page_name\":\"b6661\"},{\"extra\":{},\"page_name\":\"b6661\"},{\"page_name\":\"b6661\"}]}"
}
response = requests.post(url, headers=headers, json=data)

print(response.text)
