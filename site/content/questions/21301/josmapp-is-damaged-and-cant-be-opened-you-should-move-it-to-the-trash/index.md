+++
type = "question"
title = "&quot;JOSM.app&quot; is damaged and can&#x27;t be opened. You should move it to the Trash."
description = '''When installing JOSM on my mac, I&#x27;m seeing the error  &quot;JOSM.app&quot; is damaged and can&#x27;t be opened. You should move it to the Trash.  I am downloading the &quot;Mac OS X package&quot; from the JOSM homepage and the download appears to be succeeding without problems. Is this download &quot;damaged&quot;?'''
date = "2013-04-07T22:57:00Z"
lastmod = "2013-04-09T10:00:00Z"
weight = 21301
keywords = [ "josm" ]
aliases = [ "/questions/21301" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["JOSM.app" is damaged and can't be opened. You should move it to the Trash.](/questions/21301/josmapp-is-damaged-and-cant-be-opened-you-should-move-it-to-the-trash)

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
<span id="post-21301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21301-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When installing JOSM on my mac, I'm seeing the error</p>
<p><strong>"JOSM.app" is damaged and can't be opened. You should move it to the Trash.</strong></p>
<p><img src="https://josm.openstreetmap.de/raw-attachment/ticket/8787/damaged_josm_app.png" alt="alt text" /></p>
<p>I am downloading the "Mac OS X package" from <a href="http://josm.openstreetmap.de">the JOSM homepage</a> and the download appears to be succeeding without problems. Is this download "damaged"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '13, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '17, 22:31</strong> </span></p>
</div>
</div>
<div id="comments-container-21301" class="comments-container">
&#10;</div>
<div id="comment-tools-21301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21301-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21302"></span>

<div id="answer-container-21302" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21302-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-21302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No it's not damaged.</p>
<p>This is a highly misleading error message coming from the Gatekeeper function of OS X (10.8 Mountain Lion onwards I think (?))</p>
<p>To get round this, <strong>temporarily disable Gatekeeper</strong> as follows:</p>
<ul>
<li>open System Preferences and the 'Security &amp; Privacy' options</li>
<li>Click the padlock at the bottom if it is locked</li>
<li>Set 'Allow applications downloaded from:' to 'Anywhere'.</li>
<li>Keep that open, but go back to your finder window</li>
<li>Open JOSM.app it should work this time ...although you still get:</li>
<li>"JOSM.app" is an application downloaded from the Internet. Are you sure you want to open it? -&gt; Click 'Open'</li>
<li>Now re-enable gatekeeper back in the settings window. Put it back to the default "Mac App Store and identified developers"</li>
</ul>
<p>You won't need to do this every time you run the app. It should open fine from now on (or until you need to update)</p>
<p>Thanks to <a href="http://www.openstreetmap.org/user/drnoble/diary/17636#comments">user drnoble for his diary entry on this</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '13, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Apr '13, 23:15</strong> </span></p>
</div>
</div>
<div id="comments-container-21302" class="comments-container">
<span id="21340"></span>
<div id="comment-21340" class="comment">
<div id="post-21340-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does it cost to be an "identified developer"?</p>
</div>
<div id="comment-21340-info" class="comment-info">
<span class="comment-age">(09 Apr '13, 08:02)</span> <span class="comment-user userinfo">superduck</span>
</div>
</div>
<span id="21344"></span>
<div id="comment-21344" class="comment">
<div id="post-21344-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@superduck</span> $99 a year, see <a href="http://josm.openstreetmap.de/ticket/7904#comment:3">http://josm.openstreetmap.de/ticket/7904#comment:3</a> .</p>
</div>
<div id="comment-21344-info" class="comment-info">
<span class="comment-age">(09 Apr '13, 10:00)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-21302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21302-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

