+++
type = "question"
title = "[closed] Easy solution for lack of time tag in GPX or &quot;Found no good GPX points in input data&quot;"
description = '''So I also ran into this universal problem, as Garmin doesn&#x27;t provide &amp;lt;time&amp;gt; in GPX, nor does GPSBabel, or most things. The GPX track I had that worked was from my old Palm Pilot device over a decade ago. So I looked at it.  Turns out OpenStreetMap doesn&#x27;t even use the time stamp!!! Every time ...'''
date = "2015-02-22T04:23:00Z"
lastmod = "2015-02-23T02:56:00Z"
weight = 41227
keywords = [ "gpx", "timestamps", "good", "tag", "time" ]
aliases = [ "/questions/41227" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Easy solution for lack of time tag in GPX or "Found no good GPX points in input data"](/questions/41227/easy-solution-for-lack-of-time-tag-in-gpx-or-found-no-good-gpx-points-in-input-data)

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
<span id="post-41227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41227-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-41227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I also ran into this universal problem, as Garmin doesn't provide &lt;time&gt; in GPX, nor does GPSBabel, or most things. The GPX track I had that worked was from my old Palm Pilot device over a decade ago.</p>
<p>So I looked at it.</p>
<p>Turns out OpenStreetMap doesn't even use the time stamp!!! Every time in the working file was "1989-12-30T23:59:59Z", no difference, OSM was happy with it; it demands it, then ignores it, how dumb. *rollseyes</p>
<p>So after all the silly searching and scripts and GPS babel complex command lines, I simply did a search/replace and voilà, working GPX files that previously were erroneously rejected for time tag errors.</p>
<p>Simply open the GPX in Wordpad/Notepad/any text editor and find: <code>/ele&gt;</code></p>
<p>Replace all with: <code>/ele&gt;&lt;time&gt;1989-12-30T23:59:59Z&lt;/time&gt;</code></p>
<p>Edit sorry, this editor has issues with brackets, remove space between <code>&lt;</code> and time or /time.</p>
<p>Done. Now it'll happily take the GPX file from GPS. Hopefully future folks with this issue can search out this solution readily.</p>
<p>PS: Since the time data isn't used for anything, this should obviously be fixed, few folks have the tenacity to continue contributing when such roadblocks are presented.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-good" rel="tag" title="see questions tagged &#39;good&#39;">good</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '15, 04:23</strong></p>
<img src="https://secure.gravatar.com/avatar/afb98f6daf8f6fc1be2696777fa9108b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RJFerret&#39;s gravatar image" />
<p><span>RJFerret</span><br />
<span class="score" title="24 reputation points">24</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RJFerret has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '15, 23:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41227" class="comments-container">
<span id="41228"></span>
<div id="comment-41228" class="comment">
<div id="post-41228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow! Good work.</p>
<p>If I'm reading your post correctly, time stamps actually <strong>are</strong> required but they do not need to be incremented. Adding the same time value on all points will work.</p>
<p>I have used GPSBabel to add timestamps to old GPX files before and it is a powerful program but I agree, its command line switches frustrate me every time.</p>
<p>Cheers</p>
</div>
<div id="comment-41228-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 09:09)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="41236"></span>
<div id="comment-41236" class="comment">
<div id="post-41236-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>your search and replace does not close the time tag - which will be invalid XML. (Upd: has been fixed, see below)</p>
</div>
<div id="comment-41236-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 13:32)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="41237"></span>
<div id="comment-41237" class="comment">
<div id="post-41237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Garmin DOES provide <code>&lt;time&gt;</code> in GPX. Please use the "active track" and not saved tracks! As others said: correct time stamps are useful.</p>
<p>Yes, the OSM track upload accepts all gpx files which have at least one trackpoint with a timestamp.</p>
</div>
<div id="comment-41237-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 13:33)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="41238"></span>
<div id="comment-41238" class="comment">
<div id="post-41238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>see <a href="https://help.openstreetmap.org/questions/24550/found-no-good-gpx-points-in-the-input-data">https://help.openstreetmap.org/questions/24550/found-no-good-gpx-points-in-the-input-data</a> or <a href="https://help.openstreetmap.org/questions/35688/found-no-good-gpx-points-in-the-input-data">https://help.openstreetmap.org/questions/35688/found-no-good-gpx-points-in-the-input-data</a></p>
</div>
<div id="comment-41238-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 13:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="41249"></span>
<div id="comment-41249" class="comment not_top_scorer">
<div id="post-41249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Edited to fix the /time issue, thanks, I fought with it for a while when originally posting, it's because this editor drops stuff in brackets even with code stuff.</p>
</div>
<div id="comment-41249-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 22:51)</span> <span class="comment-user userinfo">RJFerret</span>
</div>
</div>
<span id="41252"></span>
<div id="comment-41252" class="comment">
<div id="post-41252-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10539/rjferret">@RjFerret</a>: ah, yes, but only in the preview (it is a bit fucked up...). A correctly working Markdown preview is <a href="http://daringfireball.net/projects/markdown/dingus">dingus</a>. I have removed the spaces for you.</p>
</div>
<div id="comment-41252-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 23:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="41254"></span>
<div id="comment-41254" class="comment not_top_scorer">
<div id="post-41254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have used the fake timestamps only on my own data that has been stripped of those stamps by some other application, for example, Google Earth.</p>
</div>
<div id="comment-41254-info" class="comment-info">
<span class="comment-age">(23 Feb '15, 00:01)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="41259"></span>
<div id="comment-41259" class="comment not_top_scorer">
<div id="post-41259-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-41259-info" class="comment-info">
<span class="comment-age">(23 Feb '15, 02:56)</span> <span class="comment-user userinfo">RJFerret</span>
</div>
</div>
</div>
<div id="comment-tools-41227" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-41227-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question (see links in my comment) and not a question (see https://help.openstreetmap.org/faq/ )" by aseerel4c26 22 Feb '15, 13:38

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41233"></span>

<div id="answer-container-41233" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41233-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When downloading GPS traces in JOSM you can then filter by date/time, so accurate timestamps are clearly more useful (say for example where a junction has changed and you want to ignore older traces).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '15, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-41233" class="comments-container">
&#10;</div>
<div id="comment-tools-41233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41233-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41229"></span>

<div id="answer-container-41229" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41229-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Timestamps are a witness that the track was surveyed rather than traced from a copyrighted source. It was more important when GPXes were our main source of info before Bing became a legal usable source.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '15, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-41229" class="comments-container">
&#10;</div>
<div id="comment-tools-41229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41229-form-container" class="comment-form-container">
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

