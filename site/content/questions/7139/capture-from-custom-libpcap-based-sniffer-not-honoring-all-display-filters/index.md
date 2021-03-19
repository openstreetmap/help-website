+++
type = "question"
title = "Capture from custom libpcap-based sniffer not honoring all display filters"
description = '''I &quot;inherited&quot; a custom sniffer program that is capturing traffic using libpcap. When I try to use display filters such as &quot;http.request&quot; and &quot;http.response&quot;, no traffic is displayed in Wireshark. However, when I just use &quot;http&quot;, I see all of the packets I would expect. Can anyone give me some hints ...'''
date = "2011-10-28T11:36:00Z"
lastmod = "2011-11-03T04:13:00Z"
weight = 7139
keywords = [ "filtering", "libpcap" ]
aliases = [ "/questions/7139" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Capture from custom libpcap-based sniffer not honoring all display filters](/questions/7139/capture-from-custom-libpcap-based-sniffer-not-honoring-all-display-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7139-score" class="post-score" title="current number of votes">0</div><span id="post-7139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I "inherited" a custom sniffer program that is capturing traffic using libpcap.</p><p>When I try to use display filters such as "http.request" and "http.response", no traffic is displayed in Wireshark. However, when I just use "http", I see all of the packets I would expect.</p><p>Can anyone give me some hints as to what I should be looking at more closely at this custom code that would affect the ability to use these filters? I'm not a libpcap expert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '11, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/e87a54b1689b8cbaf2703df69c49cc90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dturkel&#39;s gravatar image" /><p><span>dturkel</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dturkel has no accepted answers">0%</span></p></div></div><div id="comments-container-7139" class="comments-container"></div><div id="comment-tools-7139" class="comment-tools"></div><div class="clear"></div><div id="comment-7139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="7145"></span>

<div id="answer-container-7145" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7145-score" class="post-score" title="current number of votes">1</div><span id="post-7145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dturkel has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another option: Your sniffer program limits the capture to the first 68 bytes of the frame. Then you'll have http, but the dissector is unable to parse an http request or response field. Hence the http display filter works, http.request and http.response don't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '11, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7145" class="comments-container"><span id="7149"></span><div id="comment-7149" class="comment"><div id="post-7149-score" class="comment-score"></div><div class="comment-text"><p>The same thought occurred to me this morning over coffee. There was an option to provide the number of bytes to capture, and I increased this... and <em>bingo</em>, problem solved. Thanks very much!</p></div><div id="comment-7149-info" class="comment-info"><span class="comment-age">(29 Oct '11, 15:19)</span> <span class="comment-user userinfo">dturkel</span></div></div></div><div id="comment-tools-7145" class="comment-tools"></div><div class="clear"></div><div id="comment-7145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7140"></span>

<div id="answer-container-7140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7140-score" class="post-score" title="current number of votes">0</div><span id="post-7140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>libpcap doesn't use Wireshark <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">display filters</a>, it uses <a href="http://www.manpagez.com/man/7/pcap-filter/">capture filters</a>. It seems that your custom sniffer appends your filter string to "port ", then feeds it to libpcap. That way "port http" results in BPF filter code, while compilation of "port http.request" and "http.response" does not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '11, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7140" class="comments-container"><span id="7141"></span><div id="comment-7141" class="comment"><div id="post-7141-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap.</p><p>What I'm trying to do is select/display a capture from the custom sniffer in Wireshark, applying the display filter "http.response".<br />
</p><p>The custom sniffer does not apply any filters (which is desired, because there are quite a few other non-http filters that need to be applied as well (e.g. for SMB and other higher-level protocols).</p></div><div id="comment-7141-info" class="comment-info"><span class="comment-age">(28 Oct '11, 15:55)</span> <span class="comment-user userinfo">dturkel</span></div></div></div><div id="comment-tools-7140" class="comment-tools"></div><div class="clear"></div><div id="comment-7140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7218"></span>

<div id="answer-container-7218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7218-score" class="post-score" title="current number of votes">0</div><span id="post-7218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>libcap does not accept wireskark filters but tcpdump filters.</p><p>Look at <a href="http://justniffer.sourceforge.net/">justniffer</a> for an example of sniffer using libcap libraries</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '11, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/748d970388f03add061a45634d5608e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Augustyn&#39;s gravatar image" /><p><span>Augustyn</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Augustyn has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-7218" class="comments-container"></div><div id="comment-tools-7218" class="comment-tools"></div><div class="clear"></div><div id="comment-7218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

