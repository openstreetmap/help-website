+++
type = "question"
title = "getting PDUs length"
description = '''I want to get the PDUs length, I think it is found here: tvbuff_t *tvb -&amp;gt; length or packet_info *pinfo -&amp;gt; gssapi_decrypted_tvb -&amp;gt; length But when I compile, I get an error from the compiler: error C2037: left of &#x27;length&#x27; specifies undefined struct/union &#x27;tvbuff&#x27; Does someone know what it is...'''
date = "2013-07-03T06:27:00Z"
lastmod = "2013-07-03T11:43:00Z"
weight = 22600
keywords = [ "tvbuff_t", "pinfo", "dissector", "tcp", "wireshark" ]
aliases = [ "/questions/22600" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [getting PDUs length](/questions/22600/getting-pdus-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22600-score" class="post-score" title="current number of votes">1</div><span id="post-22600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I want to get the PDUs length, I think it is found here:</p><p><code>tvbuff_t *tvb -&gt; length</code></p><p>or</p><p><code>packet_info *pinfo -&gt; gssapi_decrypted_tvb -&gt; length</code></p><p>But when I compile, I get an error from the compiler:</p><p><code>error C2037: left of 'length' specifies undefined struct/union 'tvbuff'</code></p><p>Does someone know what it is?</p><p>member "length" exists. <a href="http://fossies.org/dox/wireshark-1.8.8/tvbuff-int_8h_source.html#l00077">you can see it here.</a></p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tvbuff_t" rel="tag" title="see questions tagged &#39;tvbuff_t&#39;">tvbuff_t</span> <span class="post-tag tag-link-pinfo" rel="tag" title="see questions tagged &#39;pinfo&#39;">pinfo</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p><span>hudac</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div></div><div id="comments-container-22600" class="comments-container"></div><div id="comment-tools-22600" class="comment-tools"></div><div class="clear"></div><div id="comment-22600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22604"></span>

<div id="answer-container-22604" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22604-score" class="post-score" title="current number of votes">2</div><span id="post-22604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hudac has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The length member is "private", to get the length use the function <code>tvb_length()</code> on a tvb pointer. Careful though, the tvb may not contain all the data expected for a PDU, e.g. because the capture was made with a small snaplen.</p><p>Also note the correct reference for Wireshark source code would be the actual Wireshark repository which can be found <a href="http://anonsvn.wireshark.org/viewvc/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22604" class="comments-container"></div><div id="comment-tools-22604" class="comment-tools"></div><div class="clear"></div><div id="comment-22604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22617"></span>

<div id="answer-container-22617" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22617-score" class="post-score" title="current number of votes">1</div><span id="post-22617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to get the PDUs length, I think it is found here:</p><pre><code>tvbuff_t *tvb -&gt; length</code></pre></blockquote><p>Remember, many capture programs, including Wireshark/TShark/dumpcap, tcpdump, and a number of other sniffers, let you limit the number of bytes captured and saved, so that if the snapshot length is N, and the packet is M bytes long, where M &gt; N, only the first N bytes of the packet will be captured.</p><p>So if you want the actual <em>packet</em> length, rather than the number of bytes of the packet that happen to have been captured, you want <code>reported_length</code>, and you get that by calling <code>tvb_reported_length()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22617" class="comments-container"></div><div id="comment-tools-22617" class="comment-tools"></div><div class="clear"></div><div id="comment-22617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

