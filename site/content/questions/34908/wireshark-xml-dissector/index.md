+++
type = "question"
title = "wireshark-xml-dissector"
description = '''Hi currently i&#x27;m writing xml and dissecting the xml through wireshark,but i&#x27;m facing with one issue if anybody help me i need to modify the below logic: nas_system_information_gsm_map = octet(1+ val(len_nas_system_information_gsm_map),  the code for this logic in attachment 1 please verify the attac...'''
date = "2014-07-25T04:58:00Z"
lastmod = "2014-07-25T05:01:00Z"
weight = 34908
keywords = [ "xml", "dissector", "wireshark" ]
aliases = [ "/questions/34908" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark-xml-dissector](/questions/34908/wireshark-xml-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34908-score" class="post-score" title="current number of votes">0</div><span id="post-34908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi currently i'm writing xml and dissecting the xml through wireshark,but i'm facing with one issue if anybody help me</p><p>i need to modify the below logic:</p><pre><code>nas_system_information_gsm_map = octet(1+ val(len_nas_system_information_gsm_map),</code></pre><p>the code for this logic in attachment 1 please verify the attachment-1 ,it contains xml code it is showing in wireshark in the below written way:</p><pre><code>len_nas_system_information_gsm_map = 111 bit (3) = 7 
nas_system_information_gsm_map = 0000 0001 bit (8) = 1</code></pre><p>but i need to implement the logic in this form :</p><pre><code>nas_system_information_gsm_map = octet(1+ val(len_nas_system_information_gsm_map)</code></pre><p>it means,this field <code>nas_system_information_gsm_map</code> has to repeat up to 8 times and it has to decode 8 bits for each iteration can any body help me how to write this logic in xml..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '14, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/7596daf4fb3556a397822344b20e2362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagar&#39;s gravatar image" /><p><span>sagar</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '14, 15:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34908" class="comments-container"><span id="34909"></span><div id="comment-34909" class="comment"><div id="post-34909-score" class="comment-score"></div><div class="comment-text"><p><a href="https://osqa-ask.wireshark.org/upfiles/sample_2.png">https://osqa-ask.wireshark.org/upfiles/sample_2.png</a> ==&gt; see the image in this link it contains xml code</p></div><div id="comment-34909-info" class="comment-info"><span class="comment-age">(25 Jul '14, 04:59)</span> <span class="comment-user userinfo">sagar</span></div></div><span id="34910"></span><div id="comment-34910" class="comment"><div id="post-34910-score" class="comment-score"></div><div class="comment-text"><p><a href="https://osqa-ask.wireshark.org/upfiles/sample2_1.png">https://osqa-ask.wireshark.org/upfiles/sample2_1.png</a> ==&gt; displaying my code snapshot in this link</p></div><div id="comment-34910-info" class="comment-info"><span class="comment-age">(25 Jul '14, 05:01)</span> <span class="comment-user userinfo">sagar</span></div></div></div><div id="comment-tools-34908" class="comment-tools"></div><div class="clear"></div><div id="comment-34908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

