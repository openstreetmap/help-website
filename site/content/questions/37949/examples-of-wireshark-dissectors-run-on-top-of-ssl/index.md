+++
type = "question"
title = "Examples of Wireshark dissectors run on top of SSL"
description = '''Just looking to see if there are already some implemented dissectors for protocols that run on top of SSL protocol. I know HTTP is one but I&#x27;m looking for other examples. It doesn&#x27;t really matter if these dissectors are standards dissectors or plugins in Wireshark.  Thanks! Flora'''
date = "2014-11-18T08:12:00Z"
lastmod = "2014-12-02T20:57:00Z"
weight = 37949
keywords = [ "ssl", "dissectors", "plugins", "wireshark" ]
aliases = [ "/questions/37949" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Examples of Wireshark dissectors run on top of SSL](/questions/37949/examples-of-wireshark-dissectors-run-on-top-of-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37949-score" class="post-score" title="current number of votes">0</div><span id="post-37949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just looking to see if there are already some implemented dissectors for protocols that run on top of SSL protocol. I know HTTP is one but I'm looking for other examples. It doesn't really matter if these dissectors are standards dissectors or plugins in Wireshark.</p><p>Thanks! Flora</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-dissectors" rel="tag" title="see questions tagged &#39;dissectors&#39;">dissectors</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '14, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-37949" class="comments-container"></div><div id="comment-tools-37949" class="comment-tools"></div><div class="clear"></div><div id="comment-37949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37950"></span>

<div id="answer-container-37950" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37950-score" class="post-score" title="current number of votes">0</div><span id="post-37950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Dissectors don't even know they're running on top of SSL, the SSL dissector uses the info in the ssl keys table to create an "association" that determines what dissector to call, looks up that dissector by name and then calls the dissector when traffic is found for that association.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '14, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37950" class="comments-container"><span id="37952"></span><div id="comment-37952" class="comment"><div id="post-37952-score" class="comment-score"></div><div class="comment-text"><p>Based on my understanding, In such this cade, dissectors should include ssl_dissector_add() which then adds the association if it is not exist. This is done in the proto_reg_handoff_xxx() instead of -for example-creating the dissector handle and then adding it by using the dissector_add_unit().</p><p>I've a question also that is related to the handoff routine as well. Why in some dissectors they include these two handles: data_handle = find_dissector("data"); http_handle = find_dissector("http"); while in others they don't? how this could be used by the dissector that runs on top of SSL ?</p><p>Thank you so much for your quick, helpful responses as usual. Flora</p></div><div id="comment-37952-info" class="comment-info"><span class="comment-age">(18 Nov '14, 10:07)</span> <span class="comment-user userinfo">flora</span></div></div><span id="37965"></span><div id="comment-37965" class="comment"><div id="post-37965-score" class="comment-score">1</div><div class="comment-text"><p>I think that dissectors call <code>ssl_dissector_add()</code> for two main reasons:</p><ul><li>The protocol normally runs over SSL when used on certain ports, e.g. https and port 443.</li><li>The protocol has a "start TLS" functionality where an unsecured connection can be converted to a secure one, e.g. ldap</li></ul></div><div id="comment-37965-info" class="comment-info"><span class="comment-age">(19 Nov '14, 02:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38288"></span><div id="comment-38288" class="comment"><div id="post-38288-score" class="comment-score"></div><div class="comment-text"><p>As usual Grahamb. If not an answer for my question, then a hint that helps to correct what I misunderstood about wireshark. Thank you so much! flora</p></div><div id="comment-38288-info" class="comment-info"><span class="comment-age">(02 Dec '14, 20:57)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-37950" class="comment-tools"></div><div class="clear"></div><div id="comment-37950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

