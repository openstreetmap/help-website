+++
type = "question"
title = "Wireshark isn&#x27;t recognizing the Skinny protocol"
description = '''Hi,  I am using the latest version of wireshark 1.8.6, after open the packet capture file, in the Protocol column, it shows TCP instead of Skinny, I know this frame is skinny traffic, maybe new bug for wireshark 1.8.6? I can provide screen dump and packet capture file. Regards Kevin'''
date = "2013-05-12T20:02:00Z"
lastmod = "2013-05-13T02:34:00Z"
weight = 21098
keywords = [ "skinny", "tcp" ]
aliases = [ "/questions/21098" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark isn't recognizing the Skinny protocol](/questions/21098/wireshark-isnt-recognizing-the-skinny-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21098-score" class="post-score" title="current number of votes">0</div><span id="post-21098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using the latest version of wireshark 1.8.6, after open the packet capture file, in the Protocol column, it shows TCP instead of Skinny, I know this frame is skinny traffic, maybe new bug for wireshark 1.8.6? I can provide screen dump and packet capture file.</p><p>Regards</p><p>Kevin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-skinny" rel="tag" title="see questions tagged &#39;skinny&#39;">skinny</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '13, 20:02</strong></p><img src="https://secure.gravatar.com/avatar/29c705861f27d90638d13963a035df7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TAC&#39;s gravatar image" /><p><span>TAC</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TAC has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '13, 15:45</strong> </span></p></div></div><div id="comments-container-21098" class="comments-container"></div><div id="comment-tools-21098" class="comment-tools"></div><div class="clear"></div><div id="comment-21098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21099"></span>

<div id="answer-container-21099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21099-score" class="post-score" title="current number of votes">1</div><span id="post-21099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark, by default, only recognizes:</p><ul><li>TCP traffic to and from port 2000;</li><li>SSL traffic to and from port 2443;</li></ul><p>as Skinny traffic. You probably have traffic to or from Yet Another Port, so you'd have to use "Decode As..." to decode it as Skinny traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '13, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21099" class="comments-container"><span id="21100"></span><div id="comment-21100" class="comment"><div id="post-21100-score" class="comment-score"></div><div class="comment-text"><p>Hi, Guy</p><p>I just checked the wireshark source code here. <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-skinny.c?view=markup">http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-skinny.c?view=markup</a> It looks like everything is defined in the packet-skinny.c file. How hard to change the wireshark default behavior and let it recognizes the Skinny traffic? I am new to Wireshark development, any guide on the web?</p></div><div id="comment-21100-info" class="comment-info"><span class="comment-age">(13 May '13, 00:31)</span> <span class="comment-user userinfo">TAC</span></div></div><span id="21103"></span><div id="comment-21103" class="comment"><div id="post-21103-score" class="comment-score">1</div><div class="comment-text"><p>"Recognize" based on what?</p><p>Wireshark can automatically recognize traffic for protocols running atop TCP or UDP based on either</p><ul><li>the TCP or UDP port number;</li><li>the contents of the packet.</li></ul><p>For the former, you'd either have a wired-in set of port numbers and have the dissector register for all those port numbers or have a preference (defaulting to the current set of port numbers) and register for the specified port numbers.</p><p>For the latter, you'd have to figure out a pattern in Skinny packets sufficient to recognize all Skinny packets <strong><em>AND</em></strong> sufficient to recognize all packets that <em>aren't</em> Skinny packets and <em>NOT</em> try to dissect them as Skinny packets.</p><p>The first of those is easy, but means that the recognition of Skinny packets is only semi-automatic - only a little better than just using "Decode As...". The latter would automatically recognize them, <em>IF</em> it's possible, but is harder, as you'd have to figure out a pattern strong enough to recognize Skinny packets as such and <em>NOT</em> to recognize non-Skinny packets.</p></div><div id="comment-21103-info" class="comment-info"><span class="comment-age">(13 May '13, 02:34)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-21099" class="comment-tools"></div><div class="clear"></div><div id="comment-21099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

