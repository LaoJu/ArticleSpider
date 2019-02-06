# -*- coding: utf-8 -*-
# @File  : zhihu_login_test3.py
# @Author: LaoJu
# @Date  : 2019/2/6
# @Desc  : 

import requests

headers = {
    # 'accept':'*/*',
    # 'accept-encoding':'gzip, deflate, br',
    # 'accept-language':'zh-CN,zh;q=0.9',
    # 'cache-control':'no-cache',
    'cookie':'tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; _zap=cf62835e-20ce-462f-ab43-d6ceeb660b07; _xsrf=753c21ee-4c0b-4e2b-992a-57374fa65e97; d_c0="AKDjiq_h8A6PTsH8-4C-qoxV43jnrOWHeBY=|1549463458"',
    # 'pragma':'no-cache',
    # 'referer':'https://www.zhihu.com/signup?next=%2F',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'x-ab-param':'tp_discussion_feed_card_type=2;pf_newguide_vertical=0;se_backsearch=0;se_premium_member=0;se_spb309=0;top_hkc_test=1;top_hotlist=1;top_new_user_rec=0;top_creator_level=0;se_consulting_price=n;se_prf=0;se_p_slideshow=0;se_sensitive=0;se_webrs=0;top_30=0;top_cc_at=1;top_test_4_liguangyi=1;tp_related_tps_movie=a;tp_sticky_android=0;zr_article_rec_rank=truncate;li_album_liutongab=0;qa_web_answerlist_ad=2;soc_bigone=0;soc_brandquestion=1;top_gif=0;top_tagextend=1;top_yhgc=0;gw_guide=0;pin_ef=orig;se_ios_spb309bugfix=0;top_root_ac=1;top_v_album=1;se_km_ad_locate=0;top_thank=1;top_universalebook=1;zr_art_rec=base;se_search_feed=N;top_brand=1;top_new_user_gift=0;top_ntr=1;top_root=0;ug_zero_follow=0;se_preset_tech=0;se_time_search=new;se_wannasearch=0;top_question_ask=1;qa_video_answer_list=0;se_daxuechuisou=new;top_login_card=1;top_recall_exp_v2=1;tp_discussion_feed_type_android=2;top_sj=2;ug_follow_answerer=0;se_colos=1;se_ios_spb309=0;soc_zero_follow=0;top_newfollow=0;top_video_rerank=-1;tp_related_topics= a;se_click2=0;se_roundtable=0;top_recall_deep_user=1;top_user_gift=0;top_promo=1;top_yc=0;se_auto_syn=0;top_ydyq=X;se_qanchor=0;se_second_search=0;top_quality=0;top_reason=1;top_sess_diversity=-1;tp_write_pin_guide=3;zr_art_rec_rank=base;tp_qa_metacard=1;se_new_market_search=on;se_new_suggest=0;se_websearch=3;se_webtimebox=0;se_zu_recommend=0;top_nucc=0;top_vidnocon=0;ls_new_video=0;top_ebook=0;top_feedre=1;top_native_answer=1;se_entity=on;se_likebutton=0;top_newfollowans=0;tp_qa_metacard_top=0;top_nad=1;top_newuser_feed=0;zr_km_material_buy=2;pf_creator_card=1;qa_answerlist_ad=0;soc_special=0;se_majorob_style=0;top_source=0;zr_rel_search=base;li_lt_tp_score=1;se_billboardsearch=0;se_zu_onebox=0;top_rank=0;zr_infinity=zr_infinity_close;top_new_feed=1;li_filter_ttl=1;se_consulting_switch=off;se_expired_ob=0;se_major_onebox=major;se_mfq=0;top_bill=0;top_core_session=-1;top_round_table=0;top_tr=0;top_wonderful=1;tp_m_intro_re_topic=0;se_minor_onebox=d;top_billpic=0;top_followtop=1;top_freecontent=1;top_rerank_reformat=-1;qa_test=0;se_ad_index=10;tp_answer_meta_guide=1;li_ts_sample=old;se_topicseed=0;se_webmajorob=0;se_wiki_box=1;zr_boost_recall=0;top_billvideo=0;top_distinction=0;zr_km_feed_rpm=default;soc_icon=1;top_card=-1;zr_ans_rec=gbrank;li_gbdt=default;pin_efs=orig;se_config=1;top_is_gr=0;tp_header_style=0;tp_sft=a;top_raf=y;se_correct_ab=0;top_billab=0;top_billupdate1=2;top_follow_reason=0;top_recall_exp_v1=1;tp_dis_version=0;zr_video_rec=zr_video_rec:base',
    # 'x-requested-with':'fetch',
    # 'x-udid':'AKDjiq_h8A6PTsH8-4C-qoxV43jnrOWHeBY=',
}

response = requests.get(url="https://www.zhihu.com/api/v3/oauth/captcha?lang=en",headers=headers)

print(response.status_code)
print(response.text)