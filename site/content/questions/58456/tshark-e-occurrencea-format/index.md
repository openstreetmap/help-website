+++
type = "question"
title = "tshark -E occurrence=a format"
description = '''I want to parse only field that I want, by Tshark using bellow tshark command: tshark -n -T fields -E header=y -E separator=, -E quote=d -E occurrence=a -e diameter.Session-Id -e diameter.cmd.code -e diameter.applicationId -e diameter.flags.request -e diameter.flags.T -e diameter.CC-Request-Type -e ...'''
date = "2017-01-02T01:31:00Z"
lastmod = "2017-01-04T22:30:00Z"
weight = 58456
keywords = [ "diameter", "parsing", "multiple", "tshark", "lua" ]
aliases = [ "/questions/58456" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -E occurrence=a format](/questions/58456/tshark-e-occurrencea-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58456-score" class="post-score" title="current number of votes">0</div><span id="post-58456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to parse only field that I want, by Tshark using bellow tshark command:</p><p><code>tshark -n -T fields -E header=y -E separator=, -E quote=d -E occurrence=a -e diameter.Session-Id -e diameter.cmd.code -e diameter.applicationId -e diameter.flags.request -e diameter.flags.T -e diameter.CC-Request-Type -e diameter.Framed-IP-Address.IPv4 -e diameter.Result-Code  -r "Diameter packet.pcap" &gt;&gt; "diameter.csv"</code></p><p>the result is</p><p><code>diameter.Session-Id diameter.cmd.code diameter.applicationId diameter.flags.request diameter.flags.T   diameter.CC-Request-Type GatewayService-5-1.spjktn002.;1481027351;2178169507,GatewayService-4-1.spjktn002.;1481029199;23273131   272,272 4,4 0,0 0,0 2,2</code></p><p>above format is difficult to be analysis and filter.</p><p>what I need is separated this information into row as bellow :</p><p><code>diameter.Session-Id    "diameter .cmd.code"  "diameter. applicationId"  "diameter. flags.request"  diameter.flags.T    diameter.CC-Request-Type    diameter.Framed-IP-Address.IPv4 diameter.Result-Code GatewayService-5-1.spjktn002.;1481027351;2178169507 272 4   0   0   2       2001 GatewayService-4-1.spjktn002.;1481029199;23273131   272 4   0   0   2       2001</code></p><p>is there any solution for my problem ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '17, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/2e4a8d9e4431f15bf082e38581181b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmulya&#39;s gravatar image" /><p><span>bmulya</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmulya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jan '17, 00:34</strong> </span></p></div></div><div id="comments-container-58456" class="comments-container"><span id="58457"></span><div id="comment-58457" class="comment"><div id="post-58457-score" class="comment-score"></div><div class="comment-text"><p>I uploaded a sample to : <a href="https://www.cloudshark.org/captures/69f3a4de2b99">https://www.cloudshark.org/captures/69f3a4de2b99</a></p></div><div id="comment-58457-info" class="comment-info"><span class="comment-age">(02 Jan '17, 01:40)</span> <span class="comment-user userinfo">bmulya</span></div></div></div><div id="comment-tools-58456" class="comment-tools"></div><div class="clear"></div><div id="comment-58456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58468"></span>

<div id="answer-container-58468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58468-score" class="post-score" title="current number of votes">1</div><span id="post-58468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I asked a similar question on this point a few years ago, where there are multiple Diameter AVP values of the same type in the same packet, and from that the intent was to generate per-record rows: <a href="https://ask.wireshark.org/questions/21428/tshark-e-output-how-to-bind-value-to-a-protocol-container">https://ask.wireshark.org/questions/21428/tshark-e-output-how-to-bind-value-to-a-protocol-container</a></p><p>In short, Tshark's -T fields option alone can't really accomplish this, since you have two Diameter-level containers in the same packet, meanwhile Tshark is just looking for all occurrances of a given attribute indiscriminately of where they appear in the packet itself.</p><p>My solution back then was to use -O, and to write a perl script to do the work of putting each unique Diameter container into its own array to then print out columns. It's likely that MATE, or a Lua script could be written to achieve something like this although I haven't personally explored either option. Tshark can't do this, though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '17, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '17, 15:38</strong> </span></p></div></div><div id="comments-container-58468" class="comments-container"><span id="58523"></span><div id="comment-58523" class="comment"><div id="post-58523-score" class="comment-score"></div><div class="comment-text"><p>is anyone can help with lua script or perl ? I have no programming skill.</p></div><div id="comment-58523-info" class="comment-info"><span class="comment-age">(04 Jan '17, 19:16)</span> <span class="comment-user userinfo">bmulya</span></div></div><span id="58527"></span><div id="comment-58527" class="comment"><div id="post-58527-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-58527-info" class="comment-info"><span class="comment-age">(04 Jan '17, 22:30)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-58468" class="comment-tools"></div><div class="clear"></div><div id="comment-58468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

