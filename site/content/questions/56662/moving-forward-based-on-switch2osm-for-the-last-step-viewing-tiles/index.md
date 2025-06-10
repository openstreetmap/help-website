+++
type = "question"
title = "Moving forward based on switch2osm for the last step Viewing tiles"
description = '''hi all,  I had at last installed ubuntu 16.04 and based on these steps from this link https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ all is working as per the link thank you for the author. I have few queries.  How to further harden this ubuntu machine and in future there is upd...'''
date = "2017-06-18T16:18:00Z"
lastmod = "2017-06-21T10:06:00Z"
weight = 56662
keywords = [ "openstreetmap", "stylesheet" ]
aliases = [ "/questions/56662" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Moving forward based on switch2osm for the last step Viewing tiles](/questions/56662/moving-forward-based-on-switch2osm-for-the-last-step-viewing-tiles)

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
<span id="post-56662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56662-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi all, I had at last installed ubuntu 16.04 and based on these steps from this link <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> all is working as per the link thank you for the author. I have few queries.</p>
<ol>
<li>How to further harden this ubuntu machine and in future there is update should I update or will it break my maps?</li>
<li>How to add more country map ? What will need to be updated I mean the steps?</li>
<li>In future when there is updates for the countries which I have included how to updated them?</li>
<li>I am stucked at this step Viewing tiles.I dont get it how to test this ? I dont get this steps We’ll add “<a href="http://tile-a.openstreetmap.fr/hot/”">http://tile-a.openstreetmap.fr/hot/”</a> as “From” and “<a href="http://yourserveripaddress/hot/”">http://yourserveripaddress/hot/”</a> as “To”, and do the same also for “tile-b” and “tile-c”.</li>
<li>How to make the openstreet map look like how the mapbox map is?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '17, 16:18</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56662" class="comments-container">
&#10;</div>
<div id="comment-tools-56662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56662-form-container" class="comment-form-container">
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

<span id="56663"></span>

<div id="answer-container-56663" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56663-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taking these one at a time:</p>
<p><strong>How to further harden this ubuntu machine and in future there is update should I update or will it break my maps?</strong></p>
<p>You shouldn't have a problem applying regular Ubuntu 16.04 LTS updates. Upgrading to 18.04 LTS (which I guess will be out early 2018) would cause a problem, as I believe that some of the stuff in the repositories used by those instructions needs updating before then. That's a year away though and will be fixed by then.</p>
<p>Whether other stuff that you may want to do to "harden" the server will break things rather depends on what you're actually doing.</p>
<p><strong>How to add more country map ? What will need to be updated I mean the steps?</strong></p>
<p>It'll likely be fastest to combine the data that you want to load into one file and then run "osm2pgsql" again with the "create" argument.</p>
<p><strong>In future when there is updates for the countries which I have included how to updated them?</strong></p>
<p>I described what you'd need to do to do that <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">here</a>. I didn't include that in the main "switch2osm" article to avoid confusing people too much.</p>
<p><strong>I am stucked at this step Viewing tiles.I dont get it how to test this ?</strong></p>
<p>This is talking about using the "switcheroo" browser extension within the Chrome or Chromium browser. If a link such as <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png</a> works then perhaps we need to explain a bit more about installing switcheroo and configuring it (once installed you have to click on the "S" that appears to the right of the addreess bar - hopefully things become more clear then).</p>
<p><strong>How to make the openstreet map look like how the mapbox map is?</strong></p>
<p>One question that immediately springs to mind is "which Mapbox map?". They have lots of different map styles. Of those styles that are publically available you'd need to check the licence file such as <a href="https://github.com/mapbox/osm-bright/blob/master/LICENSE.txt">here</a> for OSM Bright to see what you're allowed to do with it. Also some more recent Mapbox styles are designed for use with Mapbox studio rather than the tools described in the switch2osm guide. Another issue is that Mapbox may not be happy about you copying the map style that you are interested in (see <a href="https://github.com/osm2vectortiles/osm2vectortiles/issues/387">here</a> for such an issue in another map style). With any style if the licence file isn't clear enough, you'll want to check with the style's authors that it's OK to copy in this way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '17, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56663" class="comments-container">
<span id="56664"></span>
<div id="comment-56664" class="comment">
<div id="post-56664-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> 1) I plant to use this server purely to server map and nonamtim for reverse geo code. So what hardenning can I do any tips?</p>
</div>
<div id="comment-56664-info" class="comment-info">
<span class="comment-age">(18 Jun '17, 18:05)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56665"></span>
<div id="comment-56665" class="comment">
<div id="post-56665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> 2) I am not clear how to combine the data say I want to do for thailand and malaysia now. But now I have only loaded for malaysia?</p>
</div>
<div id="comment-56665-info" class="comment-info">
<span class="comment-age">(18 Jun '17, 18:06)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56666"></span>
<div id="comment-56666" class="comment">
<div id="post-56666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> 3) I am not clear on the osmosis? I know you trying to run a crontab or maybe if I want to do manually is it possible too?</p>
</div>
<div id="comment-56666-info" class="comment-info">
<span class="comment-age">(18 Jun '17, 18:09)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56667"></span>
<div id="comment-56667" class="comment">
<div id="post-56667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> 4) Can I straight move to open layers rather than doing this chrome extension?</p>
</div>
<div id="comment-56667-info" class="comment-info">
<span class="comment-age">(18 Jun '17, 18:10)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56668"></span>
<div id="comment-56668" class="comment">
<div id="post-56668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> 5) Yes I want to use osm brigh but is that permissible to use or only map box not so clear on the terms there. I saw you did before for 14.04 here is the link <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
</div>
<div id="comment-56668-info" class="comment-info">
<span class="comment-age">(18 Jun '17, 18:13)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56670"></span>
<div id="comment-56670" class="comment not_top_scorer">
<div id="post-56670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1) Not sure - someone else may be able to answer that more comprehensively</p>
<p>2) The best current suggestion for that is probably <a href="https://wiki.openstreetmap.org/wiki/Osmium">https://wiki.openstreetmap.org/wiki/Osmium</a> . Also see <a href="https://help.openstreetmap.org/questions/5389/merging-2-countries-with-osm2pgsql">https://help.openstreetmap.org/questions/5389/merging-2-countries-with-osm2pgsql</a> and <a href="https://help.openstreetmap.org/questions/19904/merging-osm-files-with-osmosis-and-import-to-postgres-with-osm2pgsql">https://help.openstreetmap.org/questions/19904/merging-osm-files-with-osmosis-and-import-to-postgres-with-osm2pgsql</a> .</p>
<p>3) Yes, you can do it manually every now and again, but if the data's significantly out of date it'll be quicker to reload rather than update.</p>
<p>4) Absolutely (or use Leaflet, which a lot of people find easier than OpenLayers).</p>
<p>5) There shouldn't be a problem with <a href="https://github.com/mapbox/osm-bright/">https://github.com/mapbox/osm-bright/</a> . Do be aware that it hasn't been updated for a year. I'd expect you'll have to solve a few problems as you go, if data that it uses has changed. Also there are a few issues with that style (such as everything with a name tag being rendered) that don't exist with some other styles.</p>
</div>
<div id="comment-56670-info" class="comment-info">
<span class="comment-age">(18 Jun '17, 18:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56698"></span>
<div id="comment-56698" class="comment not_top_scorer">
<div id="post-56698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1) Ok I will find myself on the hardening 2) I read a lot it say download osmium? The merging part I am not too sure what is the correct method many answer are with different option. So can you tell me what is the exact method? 3) I am wondering say I have run this command and again I run osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/azerbaijan-latest.osm.pbf what will happened to existing data ? Will that wiped off? I am also not sure how to rerun updates manually? 4) I am exploring both leaflet and openlayer but people saying openlayers have more features. 5) Is there any other good style sheet which you will recommend or go with the default version?</p>
</div>
<div id="comment-56698-info" class="comment-info">
<span class="comment-age">(20 Jun '17, 16:39)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56704"></span>
<div id="comment-56704" class="comment not_top_scorer">
<div id="post-56704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(answering the easy ones first)</p>
<p>3) That'll remove all data from the database and re-add the data in the file that you supply, in your example "azerbaijan-latest.osm.pbf". The answer to "how to apply updates manually" depends on how long between manual updates you plan to leave it. If you just want to catch up a day or so, then the example already mentioned at <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap</a> should work. If much longer, then I'll be quicker to reload the database than apply updates.</p>
<p>4) I think you'll find Leaflet easier.</p>
<p>5) It depends on what features you are particularly interested in showing and where in the world you are. The default OSM style is a compromise designed to work everywhere, but something else might be better for you. OSM Bright is relatively easy to modify, but you might need to fix a few minor issues to get it working as it hasn't been touched for a while.</p>
</div>
<div id="comment-56704-info" class="comment-info">
<span class="comment-age">(21 Jun '17, 09:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56705"></span>
<div id="comment-56705" class="comment not_top_scorer">
<div id="post-56705-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>2) For the merging which is the correct method to do ? I see many different google links a bit lost there.</p>
<p>3) Maybe I dont need to catch in a day or so for now. I will do manual right. What do you mean by quicket to reload the database meaning the manual way right. Another thing is that when I do the manual update is this the only step needed or any other steps need to be executed?</p>
<p>5) So which style do you recommend which does not compromise anything? I am sorry very new to all this. I also even leaflet and open layers have .css what is thay css does?</p>
</div>
<div id="comment-56705-info" class="comment-info">
<span class="comment-age">(21 Jun '17, 10:06)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
</div>
<div id="comment-tools-56663" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-56663-form-container" class="comment-form-container">
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

