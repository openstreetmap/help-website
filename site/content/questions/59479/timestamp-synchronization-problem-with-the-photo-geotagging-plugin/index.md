+++
type = "question"
title = "Timestamp synchronization problem with the Photo Geotagging plugin"
description = '''Hi, I am embarrassed to admit the photo geotagging plugin has me baffled again. I have a gps trace and a batch of photos I took during a trip I made this summer. Ordinarily, correlating the two is a simple task and I have used this tool and method countless times in the past few years. However, when...'''
date = "2017-09-08T00:51:00Z"
lastmod = "2017-09-11T14:29:00Z"
weight = 59479
keywords = [ "josm", "photo_geotagging", "plugin", "correlation", "gps" ]
aliases = [ "/questions/59479" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Timestamp synchronization problem with the Photo Geotagging plugin](/questions/59479/timestamp-synchronization-problem-with-the-photo-geotagging-plugin)

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
<span id="post-59479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59479-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am embarrassed to admit the photo geotagging plugin has me baffled again. I have a gps trace and a batch of photos I took during a trip I made this summer. Ordinarily, correlating the two is a simple task and I have used this tool and method countless times in the past few years. However, when I move operations to a new timezone, as happens every year when I move to Thailand for the winter or from Thailand back to Alaska, I cannot synchronize them. The photos and GPS trace were done in Alaska in July but I'm in Thailand now. I've tried everything I can think of: I've changed the timezone used by the plugin, changed the timezone back to Alaska Time on my computer, allowed the plugin to do its "best guess", all to no avail. I usually resort to manually synchronizing using a photo taken at a known location whenever this happens but that's tedious. I'm looking for the reason the plugin isn't able to do the deed.</p>
<p>Any help or suggestions would be appreciated.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-photo_geotagging" rel="tag" title="see questions tagged &#39;photo_geotagging&#39;">photo_geotagging</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-correlation" rel="tag" title="see questions tagged &#39;correlation&#39;">correlation</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '17, 00:51</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '17, 00:53</strong> </span></p>
</div>
</div>
<div id="comments-container-59479" class="comments-container">
&#10;</div>
<div id="comment-tools-59479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59479-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="59486"></span>

<div id="answer-container-59486" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59486-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-59486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I correlated the photos manually. I tried scai's suggestion but no matter which photo I used, including the one I shot of my GPS time, I could only get about half of them to synch. But I kept trying the "best guess" button and the more often I did that, the more photos synched. Why it doesn't get the same result each time is a mystery. Perhaps it's supposed to work that way???</p>
<p>Finally, playing with the Timezone on the plugin until the maximum number of photos synched (+9:00 hours) and playing further with the hours and minutes adjustment sliders, all 78 photos magically synched. Then I fine tuned the position further by adjusting one photo to a known location. The correction ultimately turned out to be -86602 seconds, plus the 9 hour timezone setting of course.</p>
<p>I do not understand any of this. I admit to being somewhat timezone challenged but the behavior of the plugin is baffling. In the future I'll be sure to correlate any photos before flying half way around the world.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '17, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-59486" class="comments-container">
<span id="59527"></span>
<div id="comment-59527" class="comment">
<div id="post-59527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>GPS Prune can be useful as it can display each trackpoint's time on an osm map, it will auto geo locate jpegs but if that fails the time info helps if you have to go manual. I'm tempted to upgrade to a Garmin gps with a built in camera sometimes, but dedicated cameras take better pics.</p>
</div>
<div id="comment-59527-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 08:29)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="59528"></span>
<div id="comment-59528" class="comment">
<div id="post-59528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I managed to synchronize another set of my Alaskan mapping photos using Geosetter although it was anything but an intuitive process. Then, noting that the actual positions were just slightly off I tried using the photo geotagging plugin to fine tune them but as soon as I clicked the manual adjust button and told the plugin to override GPS coords in the EXIF data (put there by Geosetter), the photos that were previously visible along the trace disappeared again and the plugin reported only 1 photo could be synchronized! The plugin is the culprit but I don't know how to even qualitatively characterize what's going on. It's either not reading or ignoring GPS data that's already in the photos.</p>
<p>I'll just go back to Geosetter and fine tune the positions there I reckon.</p>
</div>
<div id="comment-59528-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 09:44)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="59529"></span>
<div id="comment-59529" class="comment">
<div id="post-59529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe the plugin is broken for large offsets.</p>
</div>
<div id="comment-59529-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 10:22)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="59540"></span>
<div id="comment-59540" class="comment">
<div id="post-59540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I think so.</p>
<p>In the end, I was unable to fine tune the positions adequately with either program. I just used what I could and tossed the rest.</p>
<p>I might give GPSPrune a try but I used it once before and didn't like it all that much.</p>
</div>
<div id="comment-59540-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 14:25)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="59541"></span>
<div id="comment-59541" class="comment">
<div id="post-59541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It might be a good idea to open a bug at <a href="https://josm.openstreetmap.de/newticket">https://josm.openstreetmap.de/newticket</a> and provide a link to this question here (and vice versa).</p>
</div>
<div id="comment-59541-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 14:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-59486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59486-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59484"></span>

<div id="answer-container-59484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59484-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try to compare the timestamp of the first GPX point and the timestamp of the first photo's EXIF meta information. Then you will get an idea about the time difference.</p>
<p>Not sure if changing your computer's time is of any use at all since the synchronization is only done between the track and the photos.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '17, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-59484" class="comments-container">
&#10;</div>
<div id="comment-tools-59484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59484-form-container" class="comment-form-container">
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

