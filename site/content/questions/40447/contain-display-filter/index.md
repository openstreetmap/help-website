+++
type = "question"
title = "Contain display filter?"
description = '''Hello, Is there a display filter where I can search for specific ip&#x27;s or words in the info field? Thanks'''
date = "2015-03-10T11:59:00Z"
lastmod = "2015-03-11T07:08:00Z"
weight = 40447
keywords = [ "contain" ]
aliases = [ "/questions/40447" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Contain display filter?](/questions/40447/contain-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40447-score" class="post-score" title="current number of votes">0</div><span id="post-40447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is there a display filter where I can search for specific ip's or words in the info field?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-contain" rel="tag" title="see questions tagged &#39;contain&#39;">contain</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '15, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/09e8dc62bc7c0b2a6d62edf9aebb8707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gonzo&#39;s gravatar image" /><p><span>gonzo</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gonzo has no accepted answers">0%</span></p></div></div><div id="comments-container-40447" class="comments-container"></div><div id="comment-tools-40447" class="comment-tools"></div><div class="clear"></div><div id="comment-40447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="40459"></span>

<div id="answer-container-40459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40459-score" class="post-score" title="current number of votes">1</div><span id="post-40459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know there is no way to use a display filter on the contents of the Info column. However, you can use the "Find" function (ctrl-F) to search for info in the packet-list (which includes the Info column). Set your search type to string and choose "packet list" as "Search in..." option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40459" class="comments-container"></div><div id="comment-tools-40459" class="comment-tools"></div><div class="clear"></div><div id="comment-40459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40470"></span>

<div id="answer-container-40470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40470-score" class="post-score" title="current number of votes">1</div><span id="post-40470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another possibility might be to run <code>tshark</code> from the command-line and then pipe its output to <code>grep</code>. For example:</p><pre><code>tshark -r file.pcap -Y &quot;filter of interest&quot; -T fields -e frame.number -e _ws.col.Info | grep &quot;search string of interest&quot;</code></pre><p>That will give you a list of frame numbers containing your item of interest. You can then use those frame numbers as a reference when looking at packets in Wireshark (or for whatever other purpose you might have).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-40470" class="comments-container"></div><div id="comment-tools-40470" class="comment-tools"></div><div class="clear"></div><div id="comment-40470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40456"></span>

<div id="answer-container-40456" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40456-score" class="post-score" title="current number of votes">0</div><span id="post-40456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think <a href="https://wiki.wireshark.org/DisplayFilters">this</a> should get you going.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '15, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40456" class="comments-container"></div><div id="comment-tools-40456" class="comment-tools"></div><div class="clear"></div><div id="comment-40456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

