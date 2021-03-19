+++
type = "question"
title = "Dissect requests and replies"
description = '''Hello,  I am writing a dissection script for wireshark and I should point the replies/ack for specific packets. As a first implementation I create an array and write down the request ID and when a reply arrives checks if it&#x27;s ID is part of this table. I would like to print an arrow (just like ping r...'''
date = "2017-06-29T03:27:00Z"
lastmod = "2017-07-10T05:12:00Z"
weight = 62394
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/62394" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dissect requests and replies](/questions/62394/dissect-requests-and-replies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62394-score" class="post-score" title="current number of votes">1</div><span id="post-62394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am writing a dissection script for wireshark and I should point the replies/ack for specific packets. As a first implementation I create an array and write down the request ID and when a reply arrives checks if it's ID is part of this table. I would like to print an arrow (just like ping request reply) to point out the request and reply.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_20170629_131545.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '17, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/dbd6c6d55f93a7377bcbe48bfb5f0017?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyberrobot&#39;s gravatar image" /><p><span>cyberrobot</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyberrobot has no accepted answers">0%</span></p></img></div></div><div id="comments-container-62394" class="comments-container"></div><div id="comment-tools-62394" class="comment-tools"></div><div class="clear"></div><div id="comment-62394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62617"></span>

<div id="answer-container-62617" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62617-score" class="post-score" title="current number of votes">2</div><span id="post-62617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In Lua you can add two ProtoField's (one for request and one for response) for this and use frametype.REQUEST / frametype.RESPONSE as valuestring. You will get the arrows when using this fields.</p><p>Have a look in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Proto.html#lua_class_ProtoField">ProtoField</a> documentation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '17, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/193a8e6acdc05d13fb1e59fbe4eaba1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stig&#39;s gravatar image" /><p><span>stig ♦</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stig has no accepted answers">0%</span></p></div></div><div id="comments-container-62617" class="comments-container"><span id="62643"></span><div id="comment-62643" class="comment"><div id="post-62643-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply, hyperlink with framenum worked for me. Is there any elegant way to match two packets with the same sequence number?</p></div><div id="comment-62643-info" class="comment-info"><span class="comment-age">(10 Jul '17, 05:12)</span> <span class="comment-user userinfo">cyberrobot</span></div></div></div><div id="comment-tools-62617" class="comment-tools"></div><div class="clear"></div><div id="comment-62617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62396"></span>

<div id="answer-container-62396" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62396-score" class="post-score" title="current number of votes">1</div><span id="post-62396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you have to make sure to register the fields appropriately</p><p>From the ICMP dissector:</p><pre><code>             {&amp;hf_icmp_resp_in,
             {&quot;Response frame&quot;, &quot;icmp.resp_in&quot;, FT_FRAMENUM, BASE_NONE,
              FRAMENUM_TYPE(FT_FRAMENUM_RESPONSE), 0x0,
              &quot;The frame number of the corresponding response&quot;,
              HFILL}},

            {&amp;hf_icmp_resp_to,
             {&quot;Request frame&quot;, &quot;icmp.resp_to&quot;, FT_FRAMENUM, BASE_NONE,
              FRAMENUM_TYPE(FT_FRAMENUM_REQUEST), 0x0,
              &quot;The frame number of the corresponding request&quot;, HFILL}},</code></pre><p>I don't know if this can be done from LUA already.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '17, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62396" class="comments-container"></div><div id="comment-tools-62396" class="comment-tools"></div><div class="clear"></div><div id="comment-62396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

