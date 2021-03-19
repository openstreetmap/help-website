+++
type = "question"
title = "data matches regex pattern"
description = '''I&#x27;m trying to match A chat packet for a game using whatever regex wireshark uses. Apparently it&#x27;s perl but I can not get it to work... The data starts with XX:XX:19, 19 being the packet type Here are a couple of examples http://imgur.com/a/MMuDh I&#x27;ve tried thins such as the following, with no consis...'''
date = "2016-05-24T14:23:00Z"
lastmod = "2016-05-24T23:12:00Z"
weight = 52877
keywords = [ "matches", "regex", "data", "pattern" ]
aliases = [ "/questions/52877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [data matches regex pattern](/questions/52877/data-matches-regex-pattern)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52877-score" class="post-score" title="current number of votes">0</div><span id="post-52877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to match A chat packet for a game using whatever regex wireshark uses. Apparently it's perl but I can not get it to work...</p><p>The data starts with XX:XX:19, 19 being the packet type</p><p>Here are a couple of examples <a href="http://imgur.com/a/MMuDh">http://imgur.com/a/MMuDh</a></p><p>I've tried thins such as the following, with no consistency at all and im about to tear out my hair...</p><p>"..:..:19" "......19" "..:..:\x19" "\x[0-9A-F.\x[0-9A-F.\x19]</p><p>Closest I can get is just doing "\x19" but this picks up other stuff too...</p><p>Please help me out here...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-matches" rel="tag" title="see questions tagged &#39;matches&#39;">matches</span> <span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-pattern" rel="tag" title="see questions tagged &#39;pattern&#39;">pattern</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '16, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/0c70ecbbbce3f8b7cc2993b2fee0459c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pink_panther&#39;s gravatar image" /><p><span>pink_panther</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pink_panther has no accepted answers">0%</span></p></div></div><div id="comments-container-52877" class="comments-container"></div><div id="comment-tools-52877" class="comment-tools"></div><div class="clear"></div><div id="comment-52877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52880"></span>

<div id="answer-container-52880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52880-score" class="post-score" title="current number of votes">0</div><span id="post-52880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about <code>data matches ".{2}\x19"</code>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '16, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-52880" class="comments-container"><span id="52881"></span><div id="comment-52881" class="comment"><div id="post-52881-score" class="comment-score"></div><div class="comment-text"><p>This matches some stuff, but it doesnt even match the ones I'm looking for that it definitely should be matching... like the 2 in that screenshot.</p><p>If it helps i can upload a capture file to test on, this is driving me insane with its inconsistency....</p><p>Here: <a href="http://www.filedropper.com/capture_26">http://www.filedropper.com/capture_26</a></p><p>Exmaples of ones im trying to filter are: 8028, 15751, 18126, 18591, 21054, 25857, 26832, 28383, 30596</p></div><div id="comment-52881-info" class="comment-info"><span class="comment-age">(24 May '16, 15:05)</span> <span class="comment-user userinfo">pink_panther</span></div></div><span id="52882"></span><div id="comment-52882" class="comment"><div id="post-52882-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-52882-info" class="comment-info"><span class="comment-age">(24 May '16, 15:22)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52884"></span><div id="comment-52884" class="comment"><div id="post-52884-score" class="comment-score"></div><div class="comment-text"><p>OK, I hadn't looked at your screenshot; they're generally frowned upon here.</p><p>Your capture file reveals a TCP stream of data. I think your best bet is to write a dissector for the TCP payload and then you'll be able to much more easily search for the packet type using a dedicated filter for it, <code>yourchat.packet_type == 0x19</code> for example.</p><p>If you can't or don't want to write one in C, you can probably write one in Lua. You might want to look at the examples on the wiki for inspiration. See <a href="https://wiki.wireshark.org/Lua/Examples">https://wiki.wireshark.org/Lua/Examples</a></p></div><div id="comment-52884-info" class="comment-info"><span class="comment-age">(24 May '16, 16:12)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="52885"></span><div id="comment-52885" class="comment"><div id="post-52885-score" class="comment-score"></div><div class="comment-text"><p>BTW, I think the reason why <code>".{2}\x19"</code> didn't quite work is because of the \x00 preceding the \x19, and <code>.</code> won't match new-lines by default. You might try <code>data matches "(?s:.){2}\x19"</code> instead.</p><p>I still think you're better off writing a dissector for this chat protocol.</p></div><div id="comment-52885-info" class="comment-info"><span class="comment-age">(24 May '16, 16:35)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="52886"></span><div id="comment-52886" class="comment"><div id="post-52886-score" class="comment-score"></div><div class="comment-text"><p>I'll look into that..</p><p>The GUI shows the data without the : and doesnt even match "19" so i dont understand what format the data is actually in??</p><p>is it 1 hex value per line? so maybe ".{2}\n.{2}\n\x19" ?</p></div><div id="comment-52886-info" class="comment-info"><span class="comment-age">(24 May '16, 16:38)</span> <span class="comment-user userinfo">pink_panther</span></div></div><span id="52887"></span><div id="comment-52887" class="comment not_top_scorer"><div id="post-52887-score" class="comment-score"></div><div class="comment-text"><p>When I applied the <code>data matches "(?s:.){2}\x19"</code> filter on your capture file, it matched 75 frames including all the frames you listed above, namely: <em>8028, 15751, 18126, 18591, 21054, 25857, 26832, 28383, 30596</em>.</p></div><div id="comment-52887-info" class="comment-info"><span class="comment-age">(24 May '16, 16:48)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="52888"></span><div id="comment-52888" class="comment not_top_scorer"><div id="post-52888-score" class="comment-score"></div><div class="comment-text"><p>Incidentally, if you apply a slightly modified filter of <code>data matches "^(?s:.){2}\x19"</code>, then it <em>only</em> matches the frames you listed, so perhaps that's more what you're looking for?</p></div><div id="comment-52888-info" class="comment-info"><span class="comment-age">(24 May '16, 17:12)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="52894"></span><div id="comment-52894" class="comment not_top_scorer"><div id="post-52894-score" class="comment-score"></div><div class="comment-text"><blockquote><p>data.data matches "^(?s:.){2}\x19"</p></blockquote><p>Bingo bango!</p><p>Uhhhh so many thanks for this.</p><p>I thought I was good with regex, but it seems the way the data is displayed on the gui must differ from how it's actually represented.</p><p>Anyway, thank you VERY much for this. I'll be able to take it from here and do the rest of the stuff i need to do now.</p></div><div id="comment-52894-info" class="comment-info"><span class="comment-age">(24 May '16, 23:12)</span> <span class="comment-user userinfo">pink_panther</span></div></div></div><div id="comment-tools-52880" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-52880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

