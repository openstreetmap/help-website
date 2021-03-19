+++
type = "question"
title = "Type protocol (0x1a42, 0x19f0, 0x901a, 0xf735, 0x5847, etc) info ethernet II"
description = '''I want to analizy the captured traffic, but I can&#x27;t to find what kind of protocol I have. The wireshark is looking bad, it shows: Address: 1a:42:00:24:00:1e (1a:42:00:24:00:1e) Source: 1a:42:00:24:00:1e (1a:42:00:24:00:1e)  .... ...0 .... .... .... .... = IG bit: Individual address (unicast)  .... ....'''
date = "2011-06-14T01:23:00Z"
lastmod = "2011-06-20T02:40:00Z"
weight = 4555
keywords = [ "ethertype", "protocol" ]
aliases = [ "/questions/4555" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Type protocol (0x1a42, 0x19f0, 0x901a, 0xf735, 0x5847, etc) info ethernet II](/questions/4555/type-protocol-0x1a42-0x19f0-0x901a-0xf735-0x5847-etc-info-ethernet-ii)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4555-score" class="post-score" title="current number of votes">0</div><span id="post-4555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to analizy the captured traffic, but I can't to find what kind of protocol I have. The wireshark is looking bad, it shows:</p><pre><code>Address: 1a:42:00:24:00:1e (1a:42:00:24:00:1e)
Source: 1a:42:00:24:00:1e (1a:42:00:24:00:1e)
  .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
  .... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)
Type: Unknown (0x5847)</code></pre><p>What does the protocol type it can be?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethertype" rel="tag" title="see questions tagged &#39;ethertype&#39;">ethertype</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '11, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/21cc7382fe74d56a35a0215dcb888da1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Atom&#39;s gravatar image" /><p><span>Atom</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Atom has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '11, 02:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-4555" class="comments-container"></div><div id="comment-tools-4555" class="comment-tools"></div><div class="clear"></div><div id="comment-4555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4558"></span>

<div id="answer-container-4558" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4558-score" class="post-score" title="current number of votes">0</div><span id="post-4558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks as though the data link type in your capture is wrong, I doubt this is an Ethernet capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '11, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4558" class="comments-container"><span id="4560"></span><div id="comment-4560" class="comment"><div id="post-4560-score" class="comment-score"></div><div class="comment-text"><p>Wrong ? What is wrong in my capture ?</p></div><div id="comment-4560-info" class="comment-info"><span class="comment-age">(14 Jun '11, 03:05)</span> <span class="comment-user userinfo">Atom</span></div></div><span id="4561"></span><div id="comment-4561" class="comment"><div id="post-4561-score" class="comment-score"></div><div class="comment-text"><p>Every capture file has a data link type associated with it, to get a starting point for dissection. A lot of captures are done on an Ethernet, but a lot on other types of interfaces too. See <a href="http://anonsvn.wireshark.org/wireshark/trunk/wiretap/wtap.h">here</a> for a list (check for the list of WTAP_ENCAP_ values) for all possible data link types Wireshark understands. You could run the command line tool capinfos to get a better feel for the type of capture you have and post the result here.</p></div><div id="comment-4561-info" class="comment-info"><span class="comment-age">(14 Jun '11, 04:08)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="4571"></span><div id="comment-4571" class="comment"><div id="post-4571-score" class="comment-score"></div><div class="comment-text"><p>Jaap, can I show U my capture, and ask some questions ? Because I can't to understand.</p></div><div id="comment-4571-info" class="comment-info"><span class="comment-age">(15 Jun '11, 06:38)</span> <span class="comment-user userinfo">Atom</span></div></div><span id="4572"></span><div id="comment-4572" class="comment"><div id="post-4572-score" class="comment-score"></div><div class="comment-text"><p>maybe send U on e-mail...</p></div><div id="comment-4572-info" class="comment-info"><span class="comment-age">(15 Jun '11, 06:39)</span> <span class="comment-user userinfo">Atom</span></div></div><span id="4573"></span><div id="comment-4573" class="comment"><div id="post-4573-score" class="comment-score"></div><div class="comment-text"><p>and this the Ethernet capture. Maybe all the the trouble in encapsulation or in vendor of equipment?</p></div><div id="comment-4573-info" class="comment-info"><span class="comment-age">(15 Jun '11, 06:43)</span> <span class="comment-user userinfo">Atom</span></div></div><span id="4581"></span><div id="comment-4581" class="comment not_top_scorer"><div id="post-4581-score" class="comment-score"></div><div class="comment-text"><p>Sure, go ahead.</p></div><div id="comment-4581-info" class="comment-info"><span class="comment-age">(15 Jun '11, 14:34)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="4585"></span><div id="comment-4585" class="comment not_top_scorer"><div id="post-4585-score" class="comment-score"></div><div class="comment-text"><p>Can you give me your e-mail ?</p></div><div id="comment-4585-info" class="comment-info"><span class="comment-age">(15 Jun '11, 23:03)</span> <span class="comment-user userinfo">Atom</span></div></div><span id="4588"></span><div id="comment-4588" class="comment not_top_scorer"><div id="post-4588-score" class="comment-score"></div><div class="comment-text"><p>Put a little (Google) effort into it, otherwise, post yours. ;)</p></div><div id="comment-4588-info" class="comment-info"><span class="comment-age">(16 Jun '11, 02:22)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="4594"></span><div id="comment-4594" class="comment not_top_scorer"><div id="post-4594-score" class="comment-score"></div><div class="comment-text"><p>=) Jaap, can U help me or not ? I need help in this trouble... =(</p></div><div id="comment-4594-info" class="comment-info"><span class="comment-age">(16 Jun '11, 08:13)</span> <span class="comment-user userinfo">Atom</span></div></div><span id="4632"></span><div id="comment-4632" class="comment not_top_scorer"><div id="post-4632-score" class="comment-score"></div><div class="comment-text"><p>Anyone can help me ?</p></div><div id="comment-4632-info" class="comment-info"><span class="comment-age">(20 Jun '11, 02:40)</span> <span class="comment-user userinfo">Atom</span></div></div></div><div id="comment-tools-4558" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-4558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

