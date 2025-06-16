+++
type = "question"
title = "JOSM upload error on osm map that is only 20 hours old"
description = '''I downloaded a section of the OSM map from http://download.geofabrik.de/north-america.html that was only 20 hours old and I was using JOSM to move tags from a POINT to a underlying POLYGON and then deleted the POINT. When I tried to UPLOAD, I got the error &quot;Uploading failed because the server has a ...'''
date = "2016-02-27T00:17:00Z"
lastmod = "2016-02-28T16:16:00Z"
weight = 48375
keywords = [ "josm", "map", "upload", "new", "failed" ]
aliases = [ "/questions/48375" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM upload error on osm map that is only 20 hours old](/questions/48375/josm-upload-error-on-osm-map-that-is-only-20-hours-old)

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
<span id="post-48375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48375-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded a section of the OSM map from <a href="http://download.geofabrik.de/north-america.html">http://download.geofabrik.de/north-america.html</a> that was only 20 hours old and I was using JOSM to move tags from a POINT to a underlying POLYGON and then deleted the POINT. When I tried to UPLOAD, I got the error "Uploading failed because the server has a newer version of one of your nodes, ways, or relations. Click Synchronize entire dataset to synchronize the entire local dataset with the server"</p>
<p>I logged into ID EDITOR and verified that no one modified this POINT or POLYGON in the last 24 hours and cannot see why it would not upload my changes. I am new to JOSM v9329, but I though I understood uploading conflicts and how to resolve them. I am very good at ID editor. Please help, I would like to use JOSM for more off-line work on the OSM data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-new" rel="tag" title="see questions tagged &#39;new&#39;">new</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '16, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/aaf8869d4cd5c92ca9831ebf99b07eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregcrago&#39;s gravatar image" />
<p><span>gregcrago</span><br />
<span class="score" title="69 reputation points">69</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregcrago has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48375" class="comments-container">
<span id="48382"></span>
<div id="comment-48382" class="comment">
<div id="post-48382-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"only 20 hours old"? Ideally you should save / upload your changes as soon as possible, spreading larger work over multiple changesets.</p>
</div>
<div id="comment-48382-info" class="comment-info">
<span class="comment-age">(27 Feb '16, 08:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48375-form-container" class="comment-form-container">
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

<span id="48376"></span>

<div id="answer-container-48376" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48376-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-48376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That sounds like a work flow that is bound to cause issues.</p>
<p>While the the extract file might have only been 20 hours old the data is likely to have been a bit older.</p>
<p>In any case is their any reason you are not simply using the normal JOSM download mechanism?</p>
<p>With the further information you have given the picture is a bit clearer. I would point you to the POSM (see <a href="https://github.com/AmericanRedCross/posm">https://github.com/AmericanRedCross/posm</a> ) project as a potential alternative, alas I suspect that they simply haven't thought the synchronisation part of their project really through. I would suggest that you should simply accept such issues as you experienced as not avoidable and live with having to work through any conflicts on upload (you can minimize them but not completely avoid). Further splitter is really a special purpose tool and likely not suitable for generating extracts as you need them, osmosis and others are likely better suited.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '16, 00:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '16, 11:15</strong> </span></p>
</div>
</div>
<div id="comments-container-48376" class="comments-container">
<span id="48390"></span>
<div id="comment-48390" class="comment">
<div id="post-48390-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Also, why didn't you do as josm suggested and synchronize the data (file -&gt; update data/selected/modified) ? Or view the node or the polygon's history from within josm (Ctrl-h) rather than in iD ?</p>
</div>
<div id="comment-48390-info" class="comment-info">
<span class="comment-age">(27 Feb '16, 22:06)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48376-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48397"></span>

<div id="answer-container-48397" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48397-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did the .osm file come via mkgmap's "splitter" or by something else that could have removed version information (I'm guessing after reading <a href="http://www.mkgmap.org.uk/pipermail/mkgmap-dev/2016q1/024578.html">http://www.mkgmap.org.uk/pipermail/mkgmap-dev/2016q1/024578.html</a>). If so, I would expect that that would cause the problem.</p>
<p>Couldn't you instead:</p>
<ul>
<li>Download the area that you want (online) in JOSM</li>
<li>Save as a .osm</li>
<li>Work on it (offline)</li>
<li>Go back online again, update it (in case anything has changed) and then upload?</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '16, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48397" class="comments-container">
<span id="48401"></span>
<div id="comment-48401" class="comment">
<div id="post-48401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info, I've always used "osmosis" <a href="https://wiki.openstreetmap.org/wiki/Osmosis">https://wiki.openstreetmap.org/wiki/Osmosis</a> to split larger PBF downloads into smaller ones. Never tried it for editing and upload though, as (like everyone else) I've always assumed that data would be out of date too quickly.</p>
</div>
<div id="comment-48401-info" class="comment-info">
<span class="comment-age">(28 Feb '16, 14:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48403"></span>
<div id="comment-48403" class="comment">
<div id="post-48403-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd add that osmconvert will also split out a section of a larger file and may be more convenient than Osmosis. However, you still need to do some synchronisation of OSM elements with the main API DB before uploading</p>
</div>
<div id="comment-48403-info" class="comment-info">
<span class="comment-age">(28 Feb '16, 16:16)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48397-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48400"></span>

<div id="answer-container-48400" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48400-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it turns out that SPLITTER is removing dataset version information and that is why my 20 hour old data is totally different that what I downloaded.</p>
<p>I do not have internet access all the time and downloading large section of my country allow my the flexibility to use a 'splitter-type' program to break these large 'states' into smaller, JOMS sized chunks. If my dataset versions were preserved, the only UPLOAD CONFLICTs I should have would be if someone modified the exact same objects that I have modified off-line. This should not happen very often and I can deal with a few conflicts if they should arise.</p>
<p>Forcing me to use JOSM to DOWNLOAD .osm data, forces me to be online anytime I want to work on a defferent area of the country. and 'storing' .osm data is very time consuming because the maximun area you can download in JOSM is relatively small.</p>
<p>Using a TDB editor, shows me all of the splitter output files graphically and I can quickly choose a smaller .osm file to open in JOSM and start working.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '16, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/aaf8869d4cd5c92ca9831ebf99b07eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregcrago&#39;s gravatar image" />
<p><span>gregcrago</span><br />
<span class="score" title="69 reputation points">69</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregcrago has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48400" class="comments-container">
&#10;</div>
<div id="comment-tools-48400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48400-form-container" class="comment-form-container">
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

