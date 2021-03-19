+++
type = "question"
title = "how to analyse Weblogic Tuxedo Connector protocol"
description = '''i want to know how to use wireshark for analysing asynchronous protocol? '''
date = "2014-04-18T20:22:00Z"
lastmod = "2014-04-21T20:52:00Z"
weight = 31983
keywords = [ "connector", "tuxedo", "analyse", "weblogic", "protocols" ]
aliases = [ "/questions/31983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to analyse Weblogic Tuxedo Connector protocol](/questions/31983/how-to-analyse-weblogic-tuxedo-connector-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31983-score" class="post-score" title="current number of votes">0</div><span id="post-31983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to know how to use wireshark for analysing asynchronous protocol?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connector" rel="tag" title="see questions tagged &#39;connector&#39;">connector</span> <span class="post-tag tag-link-tuxedo" rel="tag" title="see questions tagged &#39;tuxedo&#39;">tuxedo</span> <span class="post-tag tag-link-analyse" rel="tag" title="see questions tagged &#39;analyse&#39;">analyse</span> <span class="post-tag tag-link-weblogic" rel="tag" title="see questions tagged &#39;weblogic&#39;">weblogic</span> <span class="post-tag tag-link-protocols" rel="tag" title="see questions tagged &#39;protocols&#39;">protocols</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '14, 20:22</strong></p><img src="https://secure.gravatar.com/avatar/885666c057a323159826c414b83eae37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fred&#39;s gravatar image" /><p><span>fred</span><br />
<span class="score" title="26 reputation points">26</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fred has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '14, 23:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-31983" class="comments-container"><span id="31986"></span><div id="comment-31986" class="comment"><div id="post-31986-score" class="comment-score"></div><div class="comment-text"><p>Do you mean "asynchronize" or "asynchronous"?</p><p>A number of protocols could be described as "asynchronous"; if you meant "asynchronous", which particular protocol do you mean?</p></div><div id="comment-31986-info" class="comment-info"><span class="comment-age">(18 Apr '14, 20:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="31987"></span><div id="comment-31987" class="comment"><div id="post-31987-score" class="comment-score"></div><div class="comment-text"><p>i made a mistake,it should be asynchronous, i want to analyse wtc protocol. WTC is that weblogic and tuxedo connect.</p></div><div id="comment-31987-info" class="comment-info"><span class="comment-age">(18 Apr '14, 20:45)</span> <span class="comment-user userinfo">fred</span></div></div></div><div id="comment-tools-31983" class="comment-tools"></div><div class="clear"></div><div id="comment-31983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31999"></span>

<div id="answer-container-31999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31999-score" class="post-score" title="current number of votes">0</div><span id="post-31999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i want to analyse wtc protocol.</p></blockquote><p>There is a BEA Tuxedo dissector in Wireshark (Display filter: tuxedo), however that seems to be a different protocol (BEA Tuxedo ATMI protocol).</p><p>So, if that is not what you are looking for (guess so), you should file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> or ask Oracle to provide a dissector for the protocol (which will probably never happen ;-))</p><p>BTW: Can you post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '14, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31999" class="comments-container"><span id="32023"></span><div id="comment-32023" class="comment"><div id="post-32023-score" class="comment-score"></div><div class="comment-text"><p>hi,Kurt first thanks for your answers. i can't post a sample capture,because those informations are very important ,they are protected.If you have interest in the issue, you can install a tuxedo and weblogic, and configure it as wtc communication method. or you could search a deamo in google.</p></div><div id="comment-32023-info" class="comment-info"><span class="comment-age">(20 Apr '14, 22:56)</span> <span class="comment-user userinfo">fred</span></div></div><span id="32026"></span><div id="comment-32026" class="comment"><div id="post-32026-score" class="comment-score"></div><div class="comment-text"><p>well, installing a whole bunch of new products, just to 'have a look' sounds like way too much work for me ;-))</p><p>BTW: If you decide to file an enhancement request, you should be prepared to either attach a sample capture file, or at least a link to the WTC protocol specs. Without that information, it's rather unlikely that anybody will take time to implement a protocol dissector. Installing the product and doing protocol reverse engineering 'just for fun' isn't completely impossible, but rather unlikely ;-)</p></div><div id="comment-32026-info" class="comment-info"><span class="comment-age">(21 Apr '14, 03:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32045"></span><div id="comment-32045" class="comment"><div id="post-32045-score" class="comment-score"></div><div class="comment-text"><p>we don't have a detailed WTC protocol specs, i search WTC protocol specs in google, but only find some simple informations. I will post some unimportant capture file.Hoping someone can figure out it.</p></div><div id="comment-32045-info" class="comment-info"><span class="comment-age">(21 Apr '14, 20:52)</span> <span class="comment-user userinfo">fred</span></div></div></div><div id="comment-tools-31999" class="comment-tools"></div><div class="clear"></div><div id="comment-31999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

