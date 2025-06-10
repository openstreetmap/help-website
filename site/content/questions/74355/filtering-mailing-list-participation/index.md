+++
type = "question"
title = "filtering mailing list participation"
description = '''A few years back, I saw a tool that allowed to see the volume of mails per OSM mailing list. it even allowed to filter by e-mail address and such. I can&#x27;t seem to find any reference at all to it anymore; Anyone have an idea, or who to ask?'''
date = "2020-04-24T12:20:00Z"
lastmod = "2020-04-24T13:18:00Z"
weight = 74355
keywords = [ "mailinglist" ]
aliases = [ "/questions/74355" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filtering mailing list participation](/questions/74355/filtering-mailing-list-participation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74355-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A few years back, I saw a tool that allowed to see the volume of mails per OSM mailing list. it even allowed to filter by e-mail address and such. I can't seem to find any reference at all to it anymore; Anyone have an idea, or who to ask?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mailinglist" rel="tag" title="see questions tagged &#39;mailinglist&#39;">mailinglist</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '20, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-74355" class="comments-container">
<span id="74356"></span>
<div id="comment-74356" class="comment">
<div id="post-74356-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not sure if this is what you're thinking about, but I might have mentioned a one-line shell script that I wrote once somewhere:</p>
<pre><code># listpeople.sh
lynx -width=1024 --dump &quot;https://lists.openstreetmap.org/pipermail/${1}/${2}-${3}/date.html#start&quot; | grep -i &quot;\[.*${1}\]&quot; | sed &quot;s/.*  //&quot; | sort | uniq -c | sort -n -r | head -20</code></pre>
<p>So "listpeople.sh osmf-talk 2020 February" will show you what name posted how many messages to a particular list in a particular month.</p>
<p>I wrote that for a giggle after someone noticed the same names cropping up on the tagging list again and again and suggested that a bit of self-selection might be in order in some cases to let everyon's voice be heard.</p>
</div>
<div id="comment-74356-info" class="comment-info">
<span class="comment-age">(24 Apr '20, 13:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74355-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

