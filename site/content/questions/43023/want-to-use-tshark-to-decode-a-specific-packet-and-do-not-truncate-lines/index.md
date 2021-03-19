+++
type = "question"
title = "Want to use tshark to decode a specific packet and do not truncate lines"
description = '''I am trying to decode a specific packet that has some lines which are long and they get truncated. I read that tshark/wireshark is compiled to have a limit of 240 characters per decode line. I see the same result using tshark or wireshark. https://www.wireshark.org/lists/wireshark-users/201003/msg00...'''
date = "2015-06-09T19:27:00Z"
lastmod = "2017-10-02T02:11:00Z"
weight = 43023
keywords = [ "decode", "tshark", "truncated" ]
aliases = [ "/questions/43023" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Want to use tshark to decode a specific packet and do not truncate lines](/questions/43023/want-to-use-tshark-to-decode-a-specific-packet-and-do-not-truncate-lines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43023-score" class="post-score" title="current number of votes">0</div><span id="post-43023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decode a specific packet that has some lines which are long and they get truncated. I read that tshark/wireshark is compiled to have a limit of 240 characters per decode line. I see the same result using tshark or wireshark.</p><p><a href="https://www.wireshark.org/lists/wireshark-users/201003/msg00155.html">https://www.wireshark.org/lists/wireshark-users/201003/msg00155.html</a></p><p>These posts were many years ago and I wanted to know if there is an option now to not truncate lines?</p><p>The options I am passing now to tshark are: -V -r &lt;file name=""&gt; -Y frame.number==&lt;packet number=""&gt;</p><p>Exmaple decode line looks like: [truncated]Authorization: Digest username="<span class="__cf_email__" data-cfemail="0a3f3f3f3f3f3f3b38393e3f3c3d32334a7a78637c6b7e6f247d7d7d24646f7e">[email protected]</span>",realm="one.www.net",nonce="55555l7kWjxkV1fRgv5555a4Vw7b5555xef5Vr5555=",algorithm=A5555-MD5,uri="sip:one.www.net",response="e900a34a51b2d183ce3f74dc59090b41",qop</p><p>I would like to use the official wireshark release and not have to recompile my own.</p><p>Thanks in advance for any help, Scott</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-truncated" rel="tag" title="see questions tagged &#39;truncated&#39;">truncated</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '15, 19:27</strong></p><img src="https://secure.gravatar.com/avatar/812690a4b3084c71abe7f917fbdd22d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jedimcclain&#39;s gravatar image" /><p><span>jedimcclain</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jedimcclain has no accepted answers">0%</span></p></div></div><div id="comments-container-43023" class="comments-container"></div><div id="comment-tools-43023" class="comment-tools"></div><div class="clear"></div><div id="comment-43023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43033"></span>

<div id="answer-container-43033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43033-score" class="post-score" title="current number of votes">1</div><span id="post-43033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is compiled to have a limit of 240 characters per decode line.</p></blockquote><p>Yes, that's correct. See my answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/23218/display-data-in-raw">https://ask.wireshark.org/questions/23218/display-data-in-raw</a></p></blockquote><p>There is currently no way, to disable truncating, other than a code change.</p><p>What you can try is this.</p><blockquote><p>tshark -nr input.pcap -T pdml</p></blockquote><p>However, I'm not sure how "-T pdml" handles the "truncate problem".</p><p>Another option would be to print the frame in HEX and extract the information with a script</p><blockquote><p>tshark -V -x -nr input.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43033" class="comments-container"></div><div id="comment-tools-43033" class="comment-tools"></div><div class="clear"></div><div id="comment-43033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43055"></span>

<div id="answer-container-43055" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43055-score" class="post-score" title="current number of votes">1</div><span id="post-43055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If there's a specific field or fields that you're interested in, then you can get the full, non-truncated output by using the <code>-T fields</code> option and specifying each field of interest with <code>-e field1</code> <code>-e field2</code> etc.</p><p>For example, I tested sending a very large syslog message and in Wireshark, if I select the truncated message, I see in the lower status bar that the field name is <code>syslog.msg</code>. Therefore, if I want to see the frame number and complete message I sent, I can run <code>tshark</code> as follows:</p><pre><code>tshark -nr syslog.pcap -Y &quot;syslog&quot; -T fields -e frame.number -e syslog.msg</code></pre><p>I specified 2 fields here just to provide an example, but you can specify any number of fields that you might need. For more details on <code>tshark</code> usage, refer to the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-43055" class="comments-container"><span id="63685"></span><div id="comment-63685" class="comment"><div id="post-63685-score" class="comment-score"></div><div class="comment-text"><p>It then truncates individual fields. I'm using <code>-Y websocket.payload -E occurrence=l -T fields -e text</code>.</p></div><div id="comment-63685-info" class="comment-info"><span class="comment-age">(02 Oct '17, 02:11)</span> <span class="comment-user userinfo">chip-devel</span></div></div></div><div id="comment-tools-43055" class="comment-tools"></div><div class="clear"></div><div id="comment-43055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

