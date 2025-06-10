+++
type = "question"
title = "Merge GPX tracks without losing data?"
description = '''I wander around with two tracking devices. I would like to merge the tracks into a single file. &quot;Solutions&quot; I&#x27;ve read really aren&#x27;t. Some merely append the tracks end to end. Another strips ALL data except lat/long (elevation and timestamps and anything else lost). I can convert to CSV, load into sp...'''
date = "2017-02-04T20:40:00Z"
lastmod = "2017-02-06T08:32:00Z"
weight = 54463
keywords = [ "merge" ]
aliases = [ "/questions/54463" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Merge GPX tracks without losing data?](/questions/54463/merge-gpx-tracks-without-losing-data)

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
<span id="post-54463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54463-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wander around with two tracking devices. I would like to merge the tracks into a single file.</p>
<p>"Solutions" I've read really aren't. Some merely append the tracks end to end. Another strips ALL data except lat/long (elevation and timestamps and anything else lost).</p>
<p>I can convert to CSV, load into spreadsheet, sort by timestamp, and convert back, but if someone else hasn't already automated this, I'd be surprised.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '17, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/4dbb88ad9ac898c20c4d084107218785?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Happy%20Hobo&#39;s gravatar image" />
<p><span>Happy Hobo</span><br />
<span class="score" title="85 reputation points">85</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Happy Hobo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54463" class="comments-container">
&#10;</div>
<div id="comment-tools-54463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54463-form-container" class="comment-form-container">
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

<span id="54466"></span>

<div id="answer-container-54466" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54466-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Happy Hobo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>GPSBabel is the Swiss Army knife of GPX editors. I found this in the manual:</p>
<p>Merge multiple tracks for the same way. This option puts all track points from all tracks into a single track and sorts them by time stamp. Points with identical time stamps will be dropped.</p>
<p>Example 4.9. Merging tracks with the track filter</p>
<p>Suppose you want to merge tracks recorded with two different GPS devices at the same time. To do that, use this command line:</p>
<p>gpsbabel -t -i gpx -f john.gpx -i gpx -f doe.gpx -x track,merge,title="COMBINED LOG" -o gpx -F john_doe.gpx</p>
<p>This example shows the command line version but it also has a GUI one can use if you prefer. The site is here:</p>
<p><a href="https://www.gpsbabel.org">https://www.gpsbabel.org</a></p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '17, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-54466" class="comments-container">
<span id="54467"></span>
<div id="comment-54467" class="comment">
<div id="post-54467-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that worked. One of the things I read suggested gpsbabel, but their method was the one that discarded all data but lat/lon. Interesting that this command for whatever reason arbitrarily split the track into several trkseg. The amusing result shows that the two devices are constantly on opposite sides of the street from each other. :-). <a href="http://www.gpsvisualizer.com/display/20170204145114-03119-map.html">http://www.gpsvisualizer.com/display/20170204145114-03119-map.html</a></p>
</div>
<div id="comment-54467-info" class="comment-info">
<span class="comment-age">(04 Feb '17, 22:49)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
<span id="54468"></span>
<div id="comment-54468" class="comment">
<div id="post-54468-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you intent to upload your tracks to OSM then don't upload this merged version. Instead upload a separate track for each of your device.</p>
</div>
<div id="comment-54468-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 09:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54470"></span>
<div id="comment-54470" class="comment">
<div id="post-54470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> - It's all data that might be useful for determining imagery offsets so whether it's loaded as one track or two, isn't the end result the same?</p>
</div>
<div id="comment-54470-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 10:00)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="54471"></span>
<div id="comment-54471" class="comment">
<div id="post-54471-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a> No, see the track visualization. At several locations the merged track jumps continuously from one side of the road to the other. The merged track is just a large mess. Uploading both tracks individually would be much better.</p>
</div>
<div id="comment-54471-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 10:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54472"></span>
<div id="comment-54472" class="comment">
<div id="post-54472-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The positional quality of one or both of these traces is low but after they're uploaded to OSM they are merely a bunch of nodes with lat/lon coordinates. GPS visualizer and even the JOSM displays show them as being "connected" but that is artificial. No such connecting lines exist in the actual data.</p>
<p>That said, the quality issue might convince me to not upload those tracks at all. How much help can such poor data actually offer to users looking to correct an imagery offset?</p>
</div>
<div id="comment-54472-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 10:39)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-54466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54466-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54474"></span>

<div id="answer-container-54474" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54474-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have also used two track recording devices at the same time. I have uploaded both ( to OSM traces as public ) on some occasions which works as a second opinion, or more when using all public traces are viewed. Currently i prefer to use GPS Prune to display both traces at the same time overlaid onto current OSM data. GPS Prune gives me the ability to delete bad points or detours into poor reception areas that are useless and "birds nest" tangles that are generated when stationary for a while. Prune also gives me the chance to edit the traces so i the only upload useful data and also avoid uploading data when I'm a little lost and drifted off a public rights of way, this iffy data could get used by mappers that haven't surveyed the area themselves, and think "someone as been there, it must be a path". I realise this isn't exactly what you asked for but hopefully it is another way to use your data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '17, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-54474" class="comments-container">
<span id="54476"></span>
<div id="comment-54476" class="comment">
<div id="post-54476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the merged result looks bad. But the problem with either track alone is that while it <em>looks</em> good, it is seriously wrong! The next step after merging is to do some smoothing. There's no point in uploading a track that is completely wrong, whether it looks good or not.</p>
</div>
<div id="comment-54476-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 13:56)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
<span id="54486"></span>
<div id="comment-54486" class="comment">
<div id="post-54486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did try to smooth the track but probably not the best algorithm. The results still sucked.</p>
</div>
<div id="comment-54486-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 20:29)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
<span id="54499"></span>
<div id="comment-54499" class="comment">
<div id="post-54499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I looked at them <a href="http://www.gpsvisualizer.com/display/20170204145114-03119-map.html">http://www.gpsvisualizer.com/display/20170204145114-03119-map.html</a> and would just delete some sections of the traces, the gps wasn't getting a good signal. Seeing that the area is a city I assume there are lots of good traces available already??. I don't think using averaging the obviously wrong points serve any purpose at all, it will just corrupt the better stuff, Human input needed in a case such as this.</p>
</div>
<div id="comment-54499-info" class="comment-info">
<span class="comment-age">(06 Feb '17, 06:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="54507"></span>
<div id="comment-54507" class="comment">
<div id="post-54507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The thought was that with one device erring northwest and one northeast that a five-point weighted average would partially cancel the errors. And it did, but the weighting I used wasn't the best. But even where the errors were smaller, along the river, the trace is consistently not on the path.</p>
</div>
<div id="comment-54507-info" class="comment-info">
<span class="comment-age">(06 Feb '17, 08:21)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
</div>
<div id="comment-tools-54474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54474-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54501"></span>

<div id="answer-container-54501" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="http://help.openstreetmap.org/upfiles/PRUNE_Speed_close_up.JPG" alt="alt text" /><img src="http://help.openstreetmap.org/upfiles/PRUNE_Speed_CrbByoZ.JPG" alt="alt text" /></p>
<p>Having seen the traces <a href="http://www.gpsvisualizer.com/display/20170204145114-03119-map.html">http://www.gpsvisualizer.com/display/20170204145114-03119-map.html</a><br />
I would guess that one device didn't have good signal all the time, was it in a pocket or a bag? high rise building can also cause problems. see <a href="http://wiki.openstreetmap.org/wiki/Accuracy_of_GPS_data">http://wiki.openstreetmap.org/wiki/Accuracy_of_GPS_data</a> I believe some devices now discard obviously faulty points, by seeing the average speed they calculate the large jumps of speed the zig zags would induce aren't likely and disregard them. It's possible this could be done with clever spread sheet, (the distance between consecutive, once a second points can't &gt; 6 km/h ( if walking) then ignore it) For me it's just easier to delete rogue points by looking at them with GPS Prune, which does display the speed between consecutive points by the way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '17, 07:06</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '17, 07:44</strong> </span></p>
</div>
</div>
<div id="comments-container-54501" class="comments-container">
<span id="54505"></span>
<div id="comment-54505" class="comment">
<div id="post-54505-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The buildings are undoubtedly part, as it is slightly better along the river. But looking at the two traces separately, one is consistently northwest of the truth and the other consistently southeast. I wasn't trying to improve the map but to have something decent for a few relatives who want to see where I wander. I knew human input would be necessary; I just want to minimize it. These are so bad that it would be more efficient to pull up a map and draw the tracks freehand. One of them, the eTrex-30, once told me its accuracy was three meters as I went out on a footpath and four meters when I came back. But the map showed the two paths fairly straight but twelve meters apart! Same device told me on another occasion after a five minute walk away from buildings that my average speed was 18 KPH.</p>
</div>
<div id="comment-54505-info" class="comment-info">
<span class="comment-age">(06 Feb '17, 08:14)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
<span id="54508"></span>
<div id="comment-54508" class="comment">
<div id="post-54508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I usually get very good results with my Garmins but i have had High rise building shadowing problems in the past. I agree, do a screen grab of OSM draw on it and send that to them.</p>
</div>
<div id="comment-54508-info" class="comment-info">
<span class="comment-age">(06 Feb '17, 08:32)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-54501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54501-form-container" class="comment-form-container">
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

