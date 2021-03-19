+++
type = "question"
title = "Preamble with MAC-LTE Dissectors"
description = '''Hi, Wireshark, I use wireshark version is 2.0.1 now. want to use MAC-LTE dissector, Preference Settings: Try Heuristic LTE-MAC framing over UDP. When send a RACH Preamble (msg1), fill length = 0, wireshark appeared: exception occurred.(other mib,sib is ok).  I reference: https://wiki.wireshark.org/M...'''
date = "2016-01-12T04:49:00Z"
lastmod = "2016-01-12T06:50:00Z"
weight = 49114
keywords = [ "mac-lte" ]
aliases = [ "/questions/49114" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Preamble with MAC-LTE Dissectors](/questions/49114/preamble-with-mac-lte-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49114-score" class="post-score" title="current number of votes">0</div><span id="post-49114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Wireshark,</p><pre><code>I use wireshark version is 2.0.1 now.
want to use MAC-LTE dissector, Preference Settings: Try Heuristic LTE-MAC framing over UDP.
When send a RACH Preamble (msg1), fill length = 0, wireshark appeared: exception occurred.(other mib,sib is ok).

I reference: https://wiki.wireshark.org/MAC-LTE.
on attachment:mac-lte1.png, the first message that I want to achieve, could you provide corresponding .pcap file for my reference.</code></pre><p>thanks, regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac-lte" rel="tag" title="see questions tagged &#39;mac-lte&#39;">mac-lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/16f68527875df52e787f82dda1c04068?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chengjingwei&#39;s gravatar image" /><p><span>chengjingwei</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chengjingwei has no accepted answers">0%</span></p></div></div><div id="comments-container-49114" class="comments-container"></div><div id="comment-tools-49114" class="comment-tools"></div><div class="clear"></div><div id="comment-49114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49116"></span>

<div id="answer-container-49116" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49116-score" class="post-score" title="current number of votes">1</div><span id="post-49116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>could you please fill a <a href="https://bugs.wireshark.org/bugzilla/">bug in our bugtracking system</a>? I'm the developer maintaining the MAC-LTE dissector and I will have a look a t it as soon as you have a pcap file.</p><p>If for whatever reason you could not access our bug system, please post here the pcap.</p><p>Edit: bug is now fixed, starting from v2.1.0rc0-1455-gb65d30d and v2.0.2rc0-34-g1b4997c. You can download pre releases from <a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '16, 06:48</strong> </span></p></div></div><div id="comments-container-49116" class="comments-container"><span id="49117"></span><div id="comment-49117" class="comment"><div id="post-49117-score" class="comment-score"></div><div class="comment-text"><p>Hi,Pascal Quantin,</p><pre><code>thank your reply, I cann&#39;t access the bug system, and I still can not confirm this is a bug, please help me here.

I need: https://wiki.wireshark.org/MAC-LTE, attachment:mac-lte1.png corresponding .pcap file, if you can provide to me, I can first analyze the problem.
or provide a include RACH Preamble (msg1)&#39;s pcap file.</code></pre><p>many thanks, regards.</p></div><div id="comment-49117-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:08)</span> <span class="comment-user userinfo">chengjingwei</span></div></div><span id="49118"></span><div id="comment-49118" class="comment"><div id="post-49118-score" class="comment-score"></div><div class="comment-text"><p>many thanks for your reply.</p></div><div id="comment-49118-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:09)</span> <span class="comment-user userinfo">chengjingwei</span></div></div><span id="49119"></span><div id="comment-49119" class="comment"><div id="post-49119-score" class="comment-score">1</div><div class="comment-text"><p>I was able to reproduce the issue myself and pushed a patch here: <a href="https://code.wireshark.org/review/#/c/13227/">https://code.wireshark.org/review/#/c/13227/</a></p></div><div id="comment-49119-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:25)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="49120"></span><div id="comment-49120" class="comment"><div id="post-49120-score" class="comment-score"></div><div class="comment-text"><p>Hi,Pascal Quantin,</p><pre><code>attachment:mac-lte1.png, as follows, I need to construct the first message(RACH).</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/mac-lte1_sHbaTEX.png" alt="alt text" /></p></div><div id="comment-49120-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:28)</span> <span class="comment-user userinfo">chengjingwei</span></div></div><span id="49121"></span><div id="comment-49121" class="comment"><div id="post-49121-score" class="comment-score"></div><div class="comment-text"><p>need to update code? I always think the issue is my own configuration parameters. I used Windows Installer (64-bit) 2.0.1, OS is windows 7 64bit. How to operate, I get code does not work.</p><p>thanks, regards</p></div><div id="comment-49121-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:36)</span> <span class="comment-user userinfo">chengjingwei</span></div></div><span id="49122"></span><div id="comment-49122" class="comment not_top_scorer"><div id="post-49122-score" class="comment-score"></div><div class="comment-text"><p>Please see my updated first reply. The screen capture from the wiki was taken before the exception issue you are seeing was introduced</p></div><div id="comment-49122-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:36)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="49123"></span><div id="comment-49123" class="comment not_top_scorer"><div id="post-49123-score" class="comment-score"></div><div class="comment-text"><p>Wait a few hours and you should have a new Windows 64 bits pre release of Wireshark 2.0.2 here: <a href="https://www.wireshark.org/download/automated/win64/">https://www.wireshark.org/download/automated/win64/</a></p><p>You should take an installer that is v2.0.2rc0-34-g1b4997c or later.</p></div><div id="comment-49123-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:47)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="49124"></span><div id="comment-49124" class="comment not_top_scorer"><div id="post-49124-score" class="comment-score"></div><div class="comment-text"><p>ok. the issue is trigger an exception in case of oob event.</p><p>Tomorrow I will go to the company to verify the new version, the problem should be solved. thank you, you are too professional.</p></div><div id="comment-49124-info" class="comment-info"><span class="comment-age">(12 Jan '16, 06:50)</span> <span class="comment-user userinfo">chengjingwei</span></div></div></div><div id="comment-tools-49116" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-49116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

