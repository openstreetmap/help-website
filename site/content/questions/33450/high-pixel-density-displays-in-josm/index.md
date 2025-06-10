+++
type = "question"
title = "High pixel density displays in JOSM"
description = '''I have a new Lenovo laptop with a high pixel density screen running Windows 8.1. These are sometimes called &quot;retina&quot; or &quot;hidpi&quot; displays and they are becoming increasingly popular as LCD panel manufacturing matures. The problem is JOSM doesn&#x27;t handle such displays gracefully. The text is so small as...'''
date = "2014-05-24T17:19:00Z"
lastmod = "2015-12-06T12:30:00Z"
weight = 33450
keywords = [ "josm", "retina", "hidpi", "display" ]
aliases = [ "/questions/33450" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [High pixel density displays in JOSM](/questions/33450/high-pixel-density-displays-in-josm)

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
<span id="post-33450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a new Lenovo laptop with a high pixel density screen running Windows 8.1. These are sometimes called "retina" or "hidpi" displays and they are becoming increasingly popular as LCD panel manufacturing matures. The problem is JOSM doesn't handle such displays gracefully. The text is so small as to be unreadable at 3200x1800 and the menus are crowded and overlap one another. Reducing the display resolution to something smaller, say 1920x1080, does not help — all text is too small and the menu system too crowded to see.</p>
<p>Is anyone else experiencing this? Is there a workaround? I looked at the JOSM Dev list and JOSM Trac site and found no references to this problem.</p>
<p>Thanks for any input you might have.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-retina" rel="tag" title="see questions tagged &#39;retina&#39;">retina</span> <span class="post-tag tag-link-hidpi" rel="tag" title="see questions tagged &#39;hidpi&#39;">hidpi</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '14, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33450" class="comments-container">
&#10;</div>
<div id="comment-tools-33450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33450-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="47013"></span>

<div id="answer-container-47013" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47013-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a known Java problem which impacts JOSM: <a href="https://josm.openstreetmap.de/query?status=!closed&amp;keywords=~high%20dpi">https://josm.openstreetmap.de/query?status=!closed&amp;keywords=~high%20dpi</a> (also tracked on <a href="https://josm.openstreetmap.de/wiki/JavaBugs">https://josm.openstreetmap.de/wiki/JavaBugs</a> )</p>
<p>changing the screen pixel count ("resolution") in the system should help as a <em>bad workaround</em>. The downside is that you would need to change it temporarily and that it will look blurry (e.g. at 1920x1080) or blocky (at 1800x900).</p>
<p>At <a href="https://bugs.openjdk.java.net/browse/JDK-8055212">https://bugs.openjdk.java.net/browse/JDK-8055212</a> we can see that at least for openJDK high dpi seems to get supported (I do not see if fully or partly) for version 9 (not sure when this will arrive in the oracle releases then). Don-vip (one of the JOSM developers) <a href="https://josm.openstreetmap.de/ticket/11806#comment:9">wrote</a> "HiDPI Graphics on Windows and Linux is covered by ​JEP 263 and may be available in ​Java 9."</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '15, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '15, 13:06</strong> </span></p>
</div>
</div>
<div id="comments-container-47013" class="comments-container">
&#10;</div>
<div id="comment-tools-47013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47013-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33454"></span>

<div id="answer-container-33454" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33454-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I resolved the problem through the use of two separate settings and thought I would pass this on so others might benefit.</p>
<p>First: right click on the screen, select Display, and set the screen resolution to 1920x1080 or something lower. The changed setting takes effect immediately for many newer Windows programs but you must convince JOSM to use it by first logging off and then logging back on. The default setting for text on these machines is set to the maximum (~200 %) at the factory so although the JOSM interface will appear more normal after the change the text in the sidebars and menus is now too big and overlaps the dialog box borders, etc.</p>
<p>Therefore the second step is to go to Control Panel&gt;Appearance and Personalization&gt;Display (right click on screen, select Personalization) and using the Change the size of all items slider reduce the size of the text to something less than maximum. I used the middle tick mark.</p>
<p>Things look much better and I can use JOSM on my new Lenovo Yoga 2 laptop.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '14, 04:58</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33454" class="comments-container">
&#10;</div>
<div id="comment-tools-33454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33454-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33451"></span>

<div id="answer-container-33451" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't comment on Windows 8.1, but Windows 7 and previous versions used to allow sizing of text on the screen separately to the display resolution, via:</p>
<ul>
<li>Right Click screen</li>
<li>Screen Resolution</li>
<li>"Making text and other items smaller or larger"</li>
</ul>
<p>You may already have done this of course and JOSM may not be honouring it, though...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '14, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33451" class="comments-container">
<span id="33453"></span>
<div id="comment-33453" class="comment">
<div id="post-33453-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My laptop is running at "max" text size already. I reckon what I'm looking for is some other way to tell JOSM that it's running in a high pixel environment.</p>
</div>
<div id="comment-33453-info" class="comment-info">
<span class="comment-age">(24 May '14, 23:13)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-33451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33451-form-container" class="comment-form-container">
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

