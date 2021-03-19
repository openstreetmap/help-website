+++
type = "question"
title = "New Plugin development"
description = '''Hi, I have just registered the plugin. But I am not sure if the dissector function is getting called. First of all is there any way to debug through logs or any other method while developing plugin. void proto_reg_handoff_c2c(void) {  static gboolean initialized = FALSE;  static dissector_handle_t c...'''
date = "2014-05-28T04:30:00Z"
lastmod = "2014-05-28T04:53:00Z"
weight = 33130
keywords = [ "dissector", "wireshark", "plugin" ]
aliases = [ "/questions/33130" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [New Plugin development](/questions/33130/new-plugin-development)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33130-score" class="post-score" title="current number of votes">0</div><span id="post-33130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have just registered the plugin. But I am not sure if the dissector function is getting called. First of all is there any way to debug through logs or any other method while developing plugin.</p><pre><code>void
proto_reg_handoff_c2c(void)
{
  static gboolean initialized = FALSE;
  static dissector_handle_t c2c_handle;
  static dissector_handle_t raw_user_handle;
  static dissector_handle_t sll_user_handle;
  static guint c2c_ethertype;
  static guint c2c_ethertype2;

  if (!initialized) {
    c2c_handle = create_dissector_handle(dissect_c2c, proto_c2c);
    raw_user_handle = create_dissector_handle(dissect_raw_user, proto_c2c);
    sll_user_handle = create_dissector_handle(dissect_sll_user, proto_c2c);
    dissector_add_handle(&quot;ethertype&quot;, c2c_handle);
//    dissector_add(&quot;wtap_encap&quot;, WTAP_ENCAP_RAW_IP, find_dissector(&quot;user_dlt&quot;));

    // The following two are needed to hook up the hacks for the wave-raw interface to wireshark
    // by taking over the RAW and SLL encapsulations.
    // This could cause trouble with &quot;real&quot; RAW or SLL captures, but can be simply fixed by deactivating the plugin.

    dissector_add(&quot;wtap_encap&quot;, WTAP_ENCAP_RAW_IP, raw_user_handle);
    dissector_add(&quot;wtap_encap&quot;, WTAP_ENCAP_SLL, sll_user_handle);

    initialized = TRUE;
  } else {
    if (c2c_ethertype != 0) {
      dissector_delete(&quot;ethertype&quot;, c2c_ethertype, c2c_handle);
    }
    if (c2c_ethertype2 != 0) {
      dissector_delete(&quot;ethertype&quot;, c2c_ethertype2, c2c_handle);
    }
  }
  if (global_c2c_ethertype != 0) {
    dissector_add(&quot;ethertype&quot;, global_c2c_ethertype, c2c_handle);
  }
  if (global_c2c_ethertype2 != 0) {
    dissector_add(&quot;ethertype&quot;, global_c2c_ethertype2, c2c_handle);
  }
  c2c_ethertype = global_c2c_ethertype;
  c2c_ethertype2 = global_c2c_ethertype2;
}</code></pre><p>The code has been provided. I have to add more dissectors. It is mentioned here that ethertype packets are going to be handled. I am not sure because I am passing the logs and I dont see anything shown in wireshark application. Please anyone could help me in this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/5a3c4db36bd55fe80a90e7fe1b9788c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amit%20Bhanja&#39;s gravatar image" /><p><span>Amit Bhanja</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amit Bhanja has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 May '14, 04:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33130" class="comments-container"><span id="33131"></span><div id="comment-33131" class="comment"><div id="post-33131-score" class="comment-score"></div><div class="comment-text"><p>You know you can have your code visualised as code by indenting it with 4 spaces? (This makes it way easier to read)</p></div><div id="comment-33131-info" class="comment-info"><span class="comment-age">(28 May '14, 04:37)</span> <span class="comment-user userinfo">xtofl</span></div></div><span id="33132"></span><div id="comment-33132" class="comment"><div id="post-33132-score" class="comment-score"></div><div class="comment-text"><p>Or by highlighting the code in question and hitting the "code" format button, or by adding the &lt; code &gt;&lt; /code &gt; tags around the code.</p><p>Keeps me busy though reformatting all the stuff.</p></div><div id="comment-33132-info" class="comment-info"><span class="comment-age">(28 May '14, 04:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="33133"></span><div id="comment-33133" class="comment"><div id="post-33133-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment, I will keep this in mind for the next time.</p></div><div id="comment-33133-info" class="comment-info"><span class="comment-age">(28 May '14, 04:53)</span> <span class="comment-user userinfo">Amit Bhanja</span></div></div></div><div id="comment-tools-33130" class="comment-tools"></div><div class="clear"></div><div id="comment-33130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

