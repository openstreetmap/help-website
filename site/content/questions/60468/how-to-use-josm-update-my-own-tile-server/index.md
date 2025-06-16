+++
type = "question"
title = "How to use Josm update my own tile server?"
description = '''Hello,I build my own tile server on my ubuntu16.04. I import a small area of mapdata to PostgreSQL.Then I use Apache and mod_tile and mapnik to render the tile.finally I use openlayer to display my Web map.  I want do some change without update my change to openstreetmap server,just edit my local ti...'''
date = "2017-11-06T08:16:00Z"
lastmod = "2017-11-06T20:40:00Z"
weight = 60468
keywords = [ "edit", "tile", "local", "serever" ]
aliases = [ "/questions/60468" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use Josm update my own tile server?](/questions/60468/how-to-use-josm-update-my-own-tile-server)

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
<span id="post-60468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,I build my own tile server on my ubuntu16.04. I import a small area of mapdata to PostgreSQL.Then I use Apache and mod_tile and mapnik to render the tile.finally I use openlayer to display my Web map. I want do some change without update my change to openstreetmap server,just edit my local tile server.I choose install Rais Port.In Josm connecting server option ,I choose :<a href="http://localhost:3000/api.But">http://localhost:3000/api.But</a> after I do some change and upload to my server.I cannot see my changes. How can I edit my local tile server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-serever" rel="tag" title="see questions tagged &#39;serever&#39;">serever</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '17, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/66e4305afae2faf808a2b600525c4cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gleide&#39;s gravatar image" />
<p><span>gleide</span><br />
<span class="score" title="79 reputation points">79</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gleide has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60468" class="comments-container">
&#10;</div>
<div id="comment-tools-60468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60468-form-container" class="comment-form-container">
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

<span id="60472"></span>

<div id="answer-container-60472" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60472-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your tile server database (likely a osm2pgsql schema DB) needs to be updated from the data in the rails port database. If it is a small area it probably doesn't make sense to use the minutely diff mechanism for updating,</p>
<p>Exporting the data in OSM XML format from the rails-port DB can likely be done with osmosis, see <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.46">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.46</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '17, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-60472" class="comments-container">
<span id="60479"></span>
<div id="comment-60479" class="comment">
<div id="post-60479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help.But I didin't express my question clearly.What I really want to do as following: In Rails Port,there are online editor like iD potlatch2,I want to edit my map and save the change to my local server not the openstreetmap server for some policy limitation.but when I save my change It asked me whether to upload to openstreetmap server,How can I only save my change on my local server but not openstreetmap server.</p>
</div>
<div id="comment-60479-info" class="comment-info">
<span class="comment-age">(06 Nov '17, 14:41)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
<span id="60487"></span>
<div id="comment-60487" class="comment">
<div id="post-60487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I completely understood that. If you are using iD on your rails-port instance you are already storing in your local DB, but as explained above wont automatically be reflected in your rendering DB.</p>
</div>
<div id="comment-60487-info" class="comment-info">
<span class="comment-age">(06 Nov '17, 20:40)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60472-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60477"></span>

<div id="answer-container-60477" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option, that may be easier than setting up the Rails port locally, is to create the file you want to update in .osc format and throw it at Osmosis. If you look <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">here</a> and at the "openstreetmap-tiles-update-expire" script you can see how that script calls Osmosis with a .osc file. Create a file in that format (e.g. from JOSM) and call Osmosis with it.</p>
<p>Also, if you're adding completely new stuff and there's not much of it, you could call osm2pgsql in append mode. See <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style-legend/blob/master/update_generated_legend.sh#L47">here</a> for an example of that in context.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '17, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60477" class="comments-container">
<span id="60480"></span>
<div id="comment-60480" class="comment">
<div id="post-60480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help.But what I really want to do is not updating my database as people edit OpenStreetMap.What I really want to do as following: In Rails Port,there are online editor like iD potlatch2,I want to edit my map online and save the change to my local server not the openstreetmap server for some policy limitation. Ｉ　would really appreciate it if you could help me solve my problem.</p>
</div>
<div id="comment-60480-info" class="comment-info">
<span class="comment-age">(06 Nov '17, 14:48)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
</div>
<div id="comment-tools-60477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60477-form-container" class="comment-form-container">
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

