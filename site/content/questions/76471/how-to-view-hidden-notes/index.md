+++
type = "question"
title = "how to view hidden notes"
description = '''The article https://wiki.openstreetmap.org/wiki/Notes#Resolving_notes says &quot;Resolved notes are not removed or deleted. After a period of seven days they are hidden from view.&quot;. But how can we view hidden notes? I did not find it. Thanks. Update: In related questions, I just saw an answer mentioning ...'''
date = "2020-09-06T01:18:00Z"
lastmod = "2023-01-07T14:11:00Z"
weight = 76471
keywords = [ "notes", "rss" ]
aliases = [ "/questions/76471" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [how to view hidden notes](/questions/76471/how-to-view-hidden-notes)

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
<span id="post-76471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76471-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-76471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The article <a href="https://wiki.openstreetmap.org/wiki/Notes#Resolving_notes">https://wiki.openstreetmap.org/wiki/Notes#Resolving_notes</a> says "Resolved notes are not removed or deleted. After a period of seven days they are hidden from view.". But how can we view hidden notes? I did not find it. Thanks.</p>
<p>Update: In related questions, I just saw an answer mentioning the RSS feed <a href="http://api.openstreetmap.org/api/0.6/notes/feed?bbox=smaller_longitude,smaller_latitude,larger_longitude,larger_latitude">http://api.openstreetmap.org/api/0.6/notes/feed?bbox=smaller_longitude,smaller_latitude,larger_longitude,larger_latitude</a> on <a href="/questions/25795/is-there-an-rss-feed-for-map-notes">https://help.openstreetmap.org/questions/25795/is-there-an-rss-feed-for-map-notes</a> but it does not show hidden notes. Maybe there is an additional parameter that needs to be used.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span> <span class="post-tag tag-link-rss" rel="tag" title="see questions tagged &#39;rss&#39;">rss</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '20, 01:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ed31503abe430abcd04be91c89b723f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baptx&#39;s gravatar image" />
<p><span>baptx</span><br />
<span class="score" title="141 reputation points">141</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baptx has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '22, 10:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-76471" class="comments-container">
&#10;</div>
<div id="comment-tools-76471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76471-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="76477"></span>

<div id="answer-container-76477" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76477-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The solution was to add <code>&amp;closed=-1</code> to <a href="http://api.openstreetmap.org/api/0.6/notes/feed?bbox=smaller_longitude,smaller_latitude,larger_longitude,larger_latitude,">http://api.openstreetmap.org/api/0.6/notes/feed?bbox=smaller_longitude,smaller_latitude,larger_longitude,larger_latitude,</a> like described here: <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API">https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API</a></p>
<p>The link is mentioned on <a href="https://wiki.openstreetmap.org/wiki/Notes/API_and_development">https://wiki.openstreetmap.org/wiki/Notes/API_and_development</a> (which is mentioned on <a href="https://wiki.openstreetmap.org/wiki/Notes">https://wiki.openstreetmap.org/wiki/Notes</a> ).</p>
<p>If there are other ways to display hidden notes, feel free to share.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '20, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ed31503abe430abcd04be91c89b723f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baptx&#39;s gravatar image" />
<p><span>baptx</span><br />
<span class="score" title="141 reputation points">141</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baptx has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '20, 12:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span></p>
</div>
</div>
<div id="comments-container-76477" class="comments-container">
<span id="83109"></span>
<div id="comment-83109" class="comment">
<div id="post-83109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you please add the rss tag to this question so it's easier for folks to find in the future?</p>
</div>
<div id="comment-83109-info" class="comment-info">
<span class="comment-age">(18 Jan '22, 03:06)</span> <span class="comment-user userinfo">ray331</span>
</div>
</div>
</div>
<div id="comment-tools-76477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76477-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76473"></span>

<div id="answer-container-76473" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76473-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, Have a look here :- <a href="http://resultmaps.neis-one.org/osm-notes">http://resultmaps.neis-one.org/osm-notes</a> scroll down select your country. Theres an option to download a file of closed notes. I've no idea how to open it on a map though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '20, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-76473" class="comments-container">
<span id="76474"></span>
<div id="comment-76474" class="comment">
<div id="post-76474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, is it an official tool from OpenStreetMap or is there another one? I noticed I can only download the RSS feed of closed notes for the last 7 days (e.g. France: <a href="https://resultmaps.neis-one.org/osm-notes-country-feed?c=France&amp;a=closed).">https://resultmaps.neis-one.org/osm-notes-country-feed?c=France&amp;a=closed).</a> How can we see notes created a few months ago? Is it possible to view notes from a specific city / area instead of a whole country? I updated my question with more details I found recently.</p>
</div>
<div id="comment-76474-info" class="comment-info">
<span class="comment-age">(06 Sep '20, 09:47)</span> <span class="comment-user userinfo">baptx</span>
</div>
</div>
</div>
<div id="comment-tools-76473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76473-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86447"></span>

<div id="answer-container-86447" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86447-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With <strong>JOSM</strong> you can easily download notes as you wish, even all closed notes, no matter how long ago they were closed.</p>
<p>To set JOSM to download notes according to your needs, you have to go to <strong>preferences (F12)</strong>, enable the <strong>Expert Mode</strong> if you haven't it enabled, click on the <strong>Advanced Preferences</strong> tab and seach for <em>notes</em>, as shown in this image:</p>
<p><img src="/upfiles/notesJOSMpreferencesChangeClosedNotesKeys2_cxU0YHj.png" alt="alt text" /></p>
<p>There, you will have several notes settings. For what you are asking, the two keys you are interested in are <strong>osm.notes.daysClosed</strong> and <strong>osm.notes.downloadLimit</strong>.</p>
<p><strong>osm.notes.daysClosed</strong>: This key lets you specify how many days closed notes should be downloaded. <strong>Default is 7</strong>, that means that JOSM would download all notes that were closed during the last 7 days. It will add, obviously, all open notes.</p>
<p>You can change that value to any other number. If you want <strong>only open notes</strong> to be downloaded, you will set it to <strong>0</strong>. And for what you are interested, if you want to <strong>download all notes, open or closed</strong>, whatever the time they were closed, you should set the value to <strong>-1</strong>.</p>
<p><strong>osm.notes.downloadLimit</strong>: This key is important because, if you are going to download all open and closed notes for a certain area, their number could be big. This key lets you decide the maximum number of notes JOSM will download. <strong>Default is 1000</strong>, but you can change it to any number from <strong>1</strong> up to <strong>10000</strong>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '23, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '23, 14:13</strong> </span></p>
</div>
</div>
<div id="comments-container-86447" class="comments-container">
&#10;</div>
<div id="comment-tools-86447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86447-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85470"></span>

<div id="answer-container-85470" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85470-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API method is simple, but requires specifying 4 coordinates (in the correct order...). In the end, I found it much easier to do with this script, where I can pass "top left URL" and "bottom right URL" from osm.org: <a href="https://github.com/richlv/osmnotes">https://github.com/richlv/osmnotes</a></p>
<p>Example:</p>
<pre><code>perl osmnotes.pl --topleft &#39;https://www.openstreetmap.org/#map=18/57.08172/24.32869&amp;layers=N&#39; --bottomright &#39;https://www.openstreetmap.org/#map=18/57.07927/24.33861&#39; --closed 70</code></pre>
<p>Disclaimer: I wrote that script some time ago.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '22, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richlv has 5 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '22, 11:52</strong> </span></p>
</div>
</div>
<div id="comments-container-85470" class="comments-container">
&#10;</div>
<div id="comment-tools-85470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85470-form-container" class="comment-form-container">
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

