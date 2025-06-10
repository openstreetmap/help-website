+++
type = "question"
title = "Need Help Installing OSM on Localhost"
description = '''I have followed the instructions here https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md at the end everything works and does as its ays it shows OSM tiles however i cannot understand or figure out how to import and use my own tiles on my own pc and not use OSM tiles pleas...'''
date = "2017-06-22T21:23:00Z"
lastmod = "2017-06-23T01:44:00Z"
weight = 56724
keywords = [ "installation" ]
aliases = [ "/questions/56724" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need Help Installing OSM on Localhost](/questions/56724/need-help-installing-osm-on-localhost)

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
<span id="post-56724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56724-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have followed the instructions here <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a> at the end everything works and does as its ays it shows OSM tiles however i cannot understand or figure out how to import and use my own tiles on my own pc and not use OSM tiles</p>
<p>please can someone give me guidence??</p>
<p>I have looked at this page <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md</a> the first part tells you to download london pdf file but i already have the pbf file I want to use so how can i use my own file and not download one mentioned?</p>
<p>i have looked at switch2osm but many of the commands are out of date so cant stall stuff using their instructions</p>
<p>I basically need an idiots guide instruction on what do do after the first instalation part</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '17, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcf952f21322c8ef39155cf811996bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gordon&#39;s gravatar image" />
<p><span>Gordon</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gordon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '17, 22:10</strong> </span></p>
</div>
</div>
<div id="comments-container-56724" class="comments-container">
<span id="56725"></span>
<div id="comment-56725" class="comment">
<div id="post-56725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a> and <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> are guides to doing very different things. If you're looking for a clone of OSM (including the ability to edit data) then you want the former; if you want to display maps, you want the latter.</p>
<p>Can you expand on the "i have looked at switch2osm but many of the commands are out of date" comment? <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> was updated very recently (to specify the database on the osm2pgsql line), so I'd be surprised if it's ot of date. Older versions of the instructions (e.g. for 14.04) I can't vouch for - by their very nature they're not "up to date".</p>
</div>
<div id="comment-56725-info" class="comment-info">
<span class="comment-age">(22 Jun '17, 23:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56727"></span>
<div id="comment-56727" class="comment">
<div id="post-56727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would like to have my own version of the whole OSM website that I can add things I want to have and show what i want on a map (basically want to have a 13th century editable map so in theory called Open13thCenturyMap). So basically identical to OSM in every way but have my own custom map. thats why i installed the <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a> as i presumed this would do what I wanted. As I said I managed to inastall as it said on that page but now I am totally confused what to do next, I been trying for a week and totally stressed and dont know what to do.</p>
<p>I went to switch and followed instructions to install mapnik but even though I did that it says "https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</p>
<p>I went to the switch site and followed instructions to install mapnik but when i check its installed it says ""importerror: no module named mapnik""</p>
</div>
<div id="comment-56727-info" class="comment-info">
<span class="comment-age">(23 Jun '17, 00:08)</span> <span class="comment-user userinfo">Gordon</span>
</div>
</div>
<span id="56728"></span>
<div id="comment-56728" class="comment">
<div id="post-56728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just just confused that I stall from one website instructions then get told to use another website instructions.</p>
<p>When i test on localhost:3000 it shows the site and osm tiles but its what i need to do after the initial install as this is where i am confused as have my own pbf file but its what do i need to do after ( just need a blank uk map that can be edited so dont need the pbf i have as it only covers a 1 square mile area) the initial install as shopwn on <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a></p>
</div>
<div id="comment-56728-info" class="comment-info">
<span class="comment-age">(23 Jun '17, 00:17)</span> <span class="comment-user userinfo">Gordon</span>
</div>
</div>
<span id="56729"></span>
<div id="comment-56729" class="comment">
<div id="post-56729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i ahev also followed instructions on this page <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md</a> When i get to OAuth Consumer Keys it asks me to log in which i cannot do as i do not have an master account, when i click create new account it sais email sent but nothing arrives but that makes sense as i am on localhost, so as you can see its one confusion after another, these instructions may be find for an expert but for a novice they make no sense</p>
</div>
<div id="comment-56729-info" class="comment-info">
<span class="comment-age">(23 Jun '17, 01:44)</span> <span class="comment-user userinfo">Gordon</span>
</div>
</div>
</div>
<div id="comment-tools-56724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56724-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

