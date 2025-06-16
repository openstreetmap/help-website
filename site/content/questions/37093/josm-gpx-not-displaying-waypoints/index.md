+++
type = "question"
title = "JOSM: gpx not displaying waypoints"
description = '''Hi I&#x27;ve a gpx downloaded from my Garmin with Basecamp &amp;amp; uploaded it to OSM via the traces webpage. I then load this GPX using the JOSM &#x27;open&#x27; dialog. It displays the trace lines &amp;amp; the nodes but not waypoints. They do display by default in P2 &amp;amp; iD.  I&#x27;ve search online &amp;amp; looked for a p...'''
date = "2014-09-28T22:15:00Z"
lastmod = "2014-09-30T13:24:00Z"
weight = 37093
keywords = [ "josm", "gpx", "waypoints", "display" ]
aliases = [ "/questions/37093" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM: gpx not displaying waypoints](/questions/37093/josm-gpx-not-displaying-waypoints)

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
<span id="post-37093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37093-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I've a gpx downloaded from my Garmin with Basecamp &amp; uploaded it to OSM via the traces webpage. I then load this GPX using the JOSM 'open' dialog. It displays the trace lines &amp; the nodes but not waypoints. They do display by default in P2 &amp; iD.</p>
<p>I've search online &amp; looked for a preference setting. What am I missing?</p>
<p>Cheers Dave F.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '14, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-37093" class="comments-container">
<span id="37139"></span>
<div id="comment-37139" class="comment">
<div id="post-37139-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you link to a public trace that shows the problem? That would help people to see what is going on.</p>
</div>
<div id="comment-37139-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 10:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37093-form-container" class="comment-form-container">
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

<span id="37095"></span>

<div id="answer-container-37095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37095-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think JOSM will display downloaded GPS data as connected dots. However, you can choose how to display "local data" if you open or Import your GPX files on your computer with JOSM directly. Their display is governed in the Preferences dialog. Go to Preferences &gt; Display &gt; GPS Points and click one of the radio buttons beneath Draw Lines between raw GPS points. I have mine set to All. This does not seem to act as I expect because only my data gets line segments. There are some other parameters you might find useful as well. I checked Draw Direction Arrows and Smooth GPX Graphics.</p>
<p>The areas governing your traces vs GPS data downloaded from the server to help setting offsets are not clearly labeled IMO but the section toward the bottom, Track and Point Coloring, deals with how the data downloaded from OSM is treated. Unlike the above, there is no option to show traces as points connected with line segments. Under that heading I chose to use color to show direction.</p>
<p>Hope that helps. There may be a way to get what you want but we'll have to wait to see if someone else can shed more light on the topic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '14, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-37095" class="comments-container">
<span id="37106"></span>
<div id="comment-37106" class="comment">
<div id="post-37106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are still some limitations with JOSM's waypoint handling when compared to e.g. Potlatch 2, though:</p>
<p><a href="/questions/7675/josm-is-it-possible-to-convert-an-individual-waypoint-in-a-gpx-file-to-a-node">https://help.openstreetmap.org/questions/7675/josm-is-it-possible-to-convert-an-individual-waypoint-in-a-gpx-file-to-a-node</a></p>
<p>I suspect that you could do something with JOSM's MapCSS support to display waypoints "nicely" - but I'm not aware of an example of that.</p>
</div>
<div id="comment-37106-info" class="comment-info">
<span class="comment-age">(29 Sep '14, 09:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37137"></span>
<div id="comment-37137" class="comment">
<div id="post-37137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks AlaskaDave, but I think you misunderstand me. It's not the lines that represent the GPX trace that aren't displaying. It's the waypoints (POIs) you can record by clicking on a button on a GPSr. See reply below.</p>
</div>
<div id="comment-37137-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 09:52)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="37143"></span>
<div id="comment-37143" class="comment">
<div id="post-37143-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>This is a Basecamp export problem. When exporting GPX traces, make sure to also copy any waypoints you wish to see later in JOSM into the same Basecamp "List". Export that List as a single GPX file. Open that file with JOSM.</p>
<p>The default color for these "Markers" as JOSM calls them is pale grey. Right click on the Markers layer in the Layers window at the left and select Customize color; set their color to white. Your waypoints are now visible. You can jump to the first one by right-clicking again and selecting Jump to next marker.</p>
<p>You cannot do this by exporting "Current" from your GPSr.</p>
</div>
<div id="comment-37143-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 11:21)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-37095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37095-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37098"></span>

<div id="answer-container-37098" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37098-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have an eTrex 30 and normally download the gpx directly from the garmin's file system instead of using Basecamp.<br />
The gpx of the track is found in /Garmin/GPX/Current or in /Garmin/GPX/Archive and the waypoint gpx of the same track is a separate file in /Garmin/GPX and is labeled like Waypoints_21-SEP-14.gpx<br />
I open both the gpx files in Josm to get the waypoints to display.<br />
(The eTrex is set to Record Method - auto, Recording Interval - most often, Auto Archive - daily)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '14, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '14, 01:17</strong> </span></p>
</div>
</div>
<div id="comments-container-37098" class="comments-container">
<span id="37138"></span>
<div id="comment-37138" class="comment">
<div id="post-37138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi nevw. Thanks for the reply. I opened my GPX directly from my GPSr (conveniently named 'current' on my unit) &amp; it displayed the waypoints! So, my next question is: What does BaseCamp change in the GPX &amp; more importantly why is JOSM unable to deal with these changes, if Potlatch &amp; iD can? After searching the web, It seems strange I appear to be the first to have flagged this up</p>
</div>
<div id="comment-37138-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 09:59)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="37140"></span>
<div id="comment-37140" class="comment">
<div id="post-37140-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The best answer to "What does BaseCamp change" would be found by opening each file (they're just XML) in a decent text editor.</p>
<p>I can't comment on Basecamp, but Mapsource changes "a whole bunch of things" - it rewrites GPX files loaded into it from an internal representation.</p>
</div>
<div id="comment-37140-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 10:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37144"></span>
<div id="comment-37144" class="comment">
<div id="post-37144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't use Basecamp, iD or P2 much but from my experience all apps have their own quirks.<br />
I did note that Basecamp does display both the trackpoints and waypoints when opening the trackpoints gpx, so it must read both gpx files on the extrex to do that. I tried exporting the displayed gpx but it did not contain the waypoints for me. Perhaps there is another way to save the gpx files from Basecamp to your filing system that include both the trackpoints and waypoints.</p>
</div>
<div id="comment-37144-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 12:02)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="37145"></span>
<div id="comment-37145" class="comment">
<div id="post-37145-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a> - yes, there is — see my comment above.</p>
</div>
<div id="comment-37145-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 12:35)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-37098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37098-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37146"></span>

<div id="answer-container-37146" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Reply to all: Thanks for your comments</p>
<p>I'm using version 7347. I think I found the problem/solution. Before trying out your suggestions, I changed Waypoint Labelling (Prefs&gt; Display Settings&gt; GPS Points) from Auto to Name &amp; the waypoints &amp; label appeared (they definitely weren't there before - I looked for the crosses). I then changed back to Auto &amp; the labels amended to include the date stamp as well as the name. I then closed JOSM &amp; started a new instance, loading the same data (Basecamp exported) as previous. The waypoints &amp; labels displayed! So it appears not to be a Basecamp, but maybe JOSM problem?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '14, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-37146" class="comments-container">
&#10;</div>
<div id="comment-tools-37146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37146-form-container" class="comment-form-container">
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

