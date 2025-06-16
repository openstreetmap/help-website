+++
type = "question"
title = "openstreetmap-website production depolyment"
description = '''i am trying to install the openstreetmap website in production, as i see in the installation and configuring page  link text,link text it is recommended to install the Phusion Passenger, CGIMap so while i was trying to figure out how to do this i have found This Docker container for OpenStreetMap We...'''
date = "2017-12-04T06:49:00Z"
lastmod = "2018-01-14T23:13:00Z"
weight = 60986
keywords = [ "installation" ]
aliases = [ "/questions/60986" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [openstreetmap-website production depolyment](/questions/60986/openstreetmap-website-production-depolyment)

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
<span id="post-60986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am trying to install the openstreetmap website in production, as i see in the installation and configuring page <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">link text</a>,<a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">link text</a> it is recommended to install the Phusion Passenger, CGIMap</p>
<p>so while i was trying to figure out how to do this i have found This Docker container for OpenStreetMap Website (aka 'Rails Port') <a href="https://github.com/geo-data/openstreetmap-website-docker">link text</a>,<a href="https://github.com/geo-data/openstreetmap-website-docker/blob/master/Dockerfile">link text</a>,<a href="https://github.com/geo-data/openstreetmap-website-docker/blob/master/run.sh">link text</a></p>
<p>but it is a bit old so i haven't been able to follow it while still use the new instructions from the official osm-website installation page</p>
<p>so can you help me and others make a good documentation with all recommendations for linux newbies like me :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '17, 06:49</strong></p>
<img src="https://secure.gravatar.com/avatar/f8c47b3830f7447fdc5ebd166eb210c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engragy&#39;s gravatar image" />
<p><span>engragy</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engragy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60986" class="comments-container">
<span id="60989"></span>
<div id="comment-60989" class="comment">
<div id="post-60989-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Can you explain what you're original goal is? The <code>openstreetmap-website</code> is not really something someone would have to deploy normally. What are you trying to do?</p>
</div>
<div id="comment-60989-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 09:32)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="60997"></span>
<div id="comment-60997" class="comment">
<div id="post-60997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi rorym I am building a geo-social website with openstreetmap in its core and as I did understand I need the api to reply for map requests and also the site will offer the ability for users to edit the map in their neighborhood</p>
</div>
<div id="comment-60997-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 16:00)</span> <span class="comment-user userinfo">engragy</span>
</div>
</div>
<span id="60998"></span>
<div id="comment-60998" class="comment">
<div id="post-60998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So to be clear - you want users to be able to contribute data to your a database at your own site, and that data won't ever go to openstreetmap.org?</p>
<p>If you do want data to be contributed to openstreetmap.org you probably need to create a different website rather than doing what you are currently doing.</p>
</div>
<div id="comment-60998-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 16:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61002"></span>
<div id="comment-61002" class="comment not_top_scorer">
<div id="post-61002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi someoneelse i do plan to upload changes in the database through josm as change sets or if i can make changes uploaded automatically that would be great, but if there is another way i would like to know about it as it will make things easier for me</p>
</div>
<div id="comment-61002-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 17:51)</span> <span class="comment-user userinfo">engragy</span>
</div>
</div>
<span id="61003"></span>
<div id="comment-61003" class="comment not_top_scorer">
<div id="post-61003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So when someone uses your website will they be updating the data at your site or at OSM?</p>
</div>
<div id="comment-61003-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 18:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61004"></span>
<div id="comment-61004" class="comment not_top_scorer">
<div id="post-61004-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the data will be updated on my website which will work for my country (egypt), but i don't know if there is something to make the changes apply to osm instantly rather than uploading changes afterwards if that is not acceptable for osm team, i really do admire the osm project and opensource projects as a whole but the reason i thought about making an osm server on localhost instead of using it is that a highspeed internet in my country is very expensive and also i read about limits for using osm because of resources</p>
</div>
<div id="comment-61004-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 18:24)</span> <span class="comment-user userinfo">engragy</span>
</div>
</div>
<span id="61005"></span>
<div id="comment-61005" class="comment">
<div id="post-61005-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want to use the data to update OSM you really want the users to be editing there directly, otherwise you'll just get into a complete mess where someone in "your" OSM has added an object, and someone in "the real" OSM has also added it, causing duplication.</p>
<p>One way to do what you want might be to host a version of iD in your website pointing at OSM, and have the maps on your site updated based on OSM minutely diffs.</p>
</div>
<div id="comment-61005-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 18:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61007"></span>
<div id="comment-61007" class="comment not_top_scorer">
<div id="post-61007-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>awesome solution, so you mean when someone make an edit it will go to real osm with minutely diffs technique and i configure a script to receive diffs for my tiles .. right</p>
</div>
<div id="comment-61007-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 18:44)</span> <span class="comment-user userinfo">engragy</span>
</div>
</div>
<span id="61008"></span>
<div id="comment-61008" class="comment">
<div id="post-61008-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nearly - they're updating OSM directly, and you update the tiles at your end based on minutely diffs. See <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap</a> for one example of how to do that.</p>
</div>
<div id="comment-61008-info" class="comment-info">
<span class="comment-age">(04 Dec '17, 18:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61087"></span>
<div id="comment-61087" class="comment not_top_scorer">
<div id="post-61087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi someoneelse can you tell me how to configure my local id editor to point the users edits to openstreetmap.org</p>
</div>
<div id="comment-61087-info" class="comment-info">
<span class="comment-age">(08 Dec '17, 12:52)</span> <span class="comment-user userinfo">engragy</span>
</div>
</div>
<span id="61088"></span>
<div id="comment-61088" class="comment not_top_scorer">
<div id="post-61088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, never done that, sorry...</p>
</div>
<div id="comment-61088-info" class="comment-info">
<span class="comment-age">(08 Dec '17, 14:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61632"></span>
<div id="comment-61632" class="comment not_top_scorer">
<div id="post-61632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I created a new question <a href="/questions/61630/how-to-change-openstreetmap-tiles-update-expire-to-use-geofabrik-updates">https://help.openstreetmap.org/questions/61630/how-to-change-openstreetmap-tiles-update-expire-to-use-geofabrik-updates</a> from a comment here.</p>
</div>
<div id="comment-61632-info" class="comment-info">
<span class="comment-age">(14 Jan '18, 23:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60986" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60986-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

