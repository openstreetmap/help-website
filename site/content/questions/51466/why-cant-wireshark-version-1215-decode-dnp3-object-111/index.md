+++
type = "question"
title = "Why can&#x27;t Wireshark version 1.2.15 decode DNP3 object 111?"
description = '''I get &quot;Unknown Object - Abort Decoding&quot; for DNP3 object 111. I know the data is correct by looking at the output from my ASE 2000 Communications test set. Most objects are decoded correctly, but some are not.'''
date = "2016-04-07T05:43:00Z"
lastmod = "2016-04-07T14:40:00Z"
weight = 51466
keywords = [ "dnp3" ]
aliases = [ "/questions/51466" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't Wireshark version 1.2.15 decode DNP3 object 111?](/questions/51466/why-cant-wireshark-version-1215-decode-dnp3-object-111)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51466-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I get "Unknown Object - Abort Decoding" for DNP3 object 111. I know the data is correct by looking at the output from my ASE 2000 Communications test set. Most objects are decoded correctly, but some are not.</p></div><div id="question-tags" class="tags-container tags">dnp3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '16, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/39808a9f0551ebf15770f4d1892f65a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DNP3Master&#39;s gravatar image" /><p>DNP3Master<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DNP3Master has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Apr '16, 08:31</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-51466" class="comments-container"><span id="51467"></span><div id="comment-51467" class="comment"><div id="post-51467-score" class="comment-score"></div><div class="comment-text"><p>It seems to be present in the code,</p><pre><code>define AL_OBJ_OCT_EVT     0x6F00   / 110 xx Octet string event /</code></pre><p>So without a look at the offeding packet it's hard to tell</p></div><div id="comment-51467-info" class="comment-info"><span class="comment-age">(07 Apr '16, 06:13)</span> Jaap ♦</div></div><span id="51470"></span><div id="comment-51470" class="comment"><div id="post-51470-score" class="comment-score"></div><div class="comment-text"><p>I added that back in 2011 (complete with erroneous comment) so it should be in 1.12.5. I'm fairly certain I've seen dissections of that object.</p><p>As @Jaap says, please share the capture with the packet somewhere publicly available.</p></div><div id="comment-51470-info" class="comment-info"><span class="comment-age">(07 Apr '16, 06:29)</span> grahamb ♦</div></div><span id="51474"></span><div id="comment-51474" class="comment"><div id="post-51474-score" class="comment-score"></div><div class="comment-text"><p>Wait, are you asking about version 1.2.15 or 1.12.something?</p><p>If you're asking about 1.2.15 then the answer is, based on Graham's comment, because the version you're running is too old.</p></div><div id="comment-51474-info" class="comment-info"><span class="comment-age">(07 Apr '16, 07:25)</span> JeffMorriss ♦</div></div><span id="51475"></span><div id="comment-51475" class="comment"><div id="post-51475-score" class="comment-score"></div><div class="comment-text"><p>Oops, unable to parse the version numbers, my brain couldn't believe someone is still running 1.2.15 (built 1st March 2011).</p></div><div id="comment-51475-info" class="comment-info"><span class="comment-age">(07 Apr '16, 07:40)</span> grahamb ♦</div></div><span id="51476"></span><div id="comment-51476" class="comment"><div id="post-51476-score" class="comment-score"></div><div class="comment-text"><blockquote><p>1.2.15 (built 1st March 2011).</p></blockquote><p>... which (for DNP3Master's benefit) would <em>not</em> include enhancements (like decoding this object) checked in in 2011 since 1.2 was one of the stable branches at the time.</p></div><div id="comment-51476-info" class="comment-info"><span class="comment-age">(07 Apr '16, 07:53)</span> JeffMorriss ♦</div></div><span id="51479"></span><div id="comment-51479" class="comment not_top_scorer"><div id="post-51479-score" class="comment-score"></div><div class="comment-text"><p>Oh, forgot to mention:</p><blockquote><p>Oops, unable to parse the version numbers, my brain couldn't believe someone is still running 1.2.15</p></blockquote><p>That's because you haven't spent the past N years of your life living in RHEL/CentOS 6 (which shipped with 1.2 and has stayed on 1.2--though <a href="http://rpms.famillecollet.com/rpmphp/zoom.php?rpm=wireshark">http://rpms.famillecollet.com/rpmphp/zoom.php?rpm=wireshark</a> seems to indicate that RHEL 6 has actually upgraded to 1.8.</p></div><div id="comment-51479-info" class="comment-info"><span class="comment-age">(07 Apr '16, 07:56)</span> JeffMorriss ♦</div></div><span id="51480"></span><div id="comment-51480" class="comment not_top_scorer"><div id="post-51480-score" class="comment-score"></div><div class="comment-text"><p>@JeffMorris</p><blockquote>That's because you haven't spent the past N years of your life living in RHEL/CentOS 6</blockquote><p>Thankfully. Presumably there's folks planning to continue with the next 2N years of their life on RHEL6.</p></div><div id="comment-51480-info" class="comment-info"><span class="comment-age">(07 Apr '16, 08:01)</span> grahamb ♦</div></div></div><div id="comment-tools-51466" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-51466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51496"></span>

<div id="answer-container-51496" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51496-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the comments it becomes clear that the relevant dissection wasn't yet implemented in that old Wireshark version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '16, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-51496" class="comments-container"></div><div id="comment-tools-51496" class="comment-tools"></div><div class="clear"></div><div id="comment-51496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

