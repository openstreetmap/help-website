+++
type = "question"
title = "How to investigate missing amenities?"
description = '''Hello, Several months (maybe an year?) ago I had thoroughly mapped an area. Now as I check it, all the amenities are missing. It was a square with pharmacies, shops, banks, marketplace, parkings - various stuff. highway ways are intact, but maybe about 20 tagged nodes and polygons are gone. I tried ...'''
date = "2016-04-04T17:51:00Z"
lastmod = "2016-04-05T16:51:00Z"
weight = 49020
keywords = [ "data", "history" ]
aliases = [ "/questions/49020" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to investigate missing amenities?](/questions/49020/how-to-investigate-missing-amenities)

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
<span id="post-49020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49020-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Several months (maybe an year?) ago I had thoroughly mapped an area. Now as I check it, all the amenities are missing. It was a square with pharmacies, shops, banks, marketplace, parkings - various stuff.</p>
<p><code>highway</code> ways are intact, but maybe about 20 tagged nodes and polygons are gone. I tried looking at the <a href="http://www.openstreetmap.org/history#map=19/42.15083/24.74497">history</a>, but it is full of bogus edits that have nothing to do with my area. It shows worldwide changesets that happen to contain my area as well and it is not usable at all.</p>
<p>How can I proceed to find out what happened to all the stuff there?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '16, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Apr '16, 17:52</strong> </span></p>
</div>
</div>
<div id="comments-container-49020" class="comments-container">
&#10;</div>
<div id="comment-tools-49020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49020-form-container" class="comment-form-container">
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

<span id="49027"></span>

<div id="answer-container-49027" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49027-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-49027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivanatora has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API has some features for restricting queries based on date and time:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Attic_data_.28.22date.22.29">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Attic_data_.28.22date.22.29</a></p>
<p>Here's an example showing amenities that existed on a given date:</p>
<p><a href="http://overpass-turbo.eu/s/fsj">http://overpass-turbo.eu/s/fsj</a></p>
<p>And another showing items that were edited during a period of time:</p>
<p><a href="http://overpass-turbo.eu/s/fso">http://overpass-turbo.eu/s/fso</a></p>
<p>Edit: The examples queries above only specify the date. As explained further in the comments below, to get correct results it is necessary to specify the date and time, like "2015-01-01T06:55:00Z".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '16, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Apr '16, 16:54</strong> </span></p>
</div>
</div>
<div id="comments-container-49027" class="comments-container">
<span id="49028"></span>
<div id="comment-49028" class="comment">
<div id="post-49028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>wow, that's cool! sadly turbo is not working since some days :( Firefox' console shows a blocked cross-origin request to the interpreter. Not for you? hmm...</p>
</div>
<div id="comment-49028-info" class="comment-info">
<span class="comment-age">(04 Apr '16, 20:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49029"></span>
<div id="comment-49029" class="comment">
<div id="post-49029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> Sounds like a bug at your end - <a href="http://overpass-turbo.eu/s/fsj">http://overpass-turbo.eu/s/fsj</a> works for me in Firefox, Chrome and Seamonkey (all Windows 7).</p>
</div>
<div id="comment-49029-info" class="comment-info">
<span class="comment-age">(04 Apr '16, 21:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49030"></span>
<div id="comment-49030" class="comment">
<div id="post-49030-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: Ah, thanks! I digged a bit deeper: The request was made to <a href="http://overpass-api.de">http://overpass-api.de</a> and was rewritten to <a href="https://overpass-api.de">https://overpass-api.de</a> by a browser plugin. Either some plugin is not working correctly with another one, or... whatever. Opening overpass-turbo via https fixes the issue. :) If you think this is not useful for others, please delete my comments.</p>
</div>
<div id="comment-49030-info" class="comment-info">
<span class="comment-age">(04 Apr '16, 21:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49038"></span>
<div id="comment-49038" class="comment not_top_scorer">
<div id="post-49038-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this really working? Because, I'm trying this <a href="http://overpass-turbo.eu/s/ftx">http://overpass-turbo.eu/s/ftx</a> with date 2015-01-01 and it returns amenities I've created yesterday.</p>
</div>
<div id="comment-49038-info" class="comment-info">
<span class="comment-age">(05 Apr '16, 14:49)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="49039"></span>
<div id="comment-49039" class="comment not_top_scorer">
<div id="post-49039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For me that query returns exactly three things, all created before 2015-01-01. Look at what's highlighted at the right, not at the data on the map tiles...</p>
</div>
<div id="comment-49039-info" class="comment-info">
<span class="comment-age">(05 Apr '16, 14:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49041"></span>
<div id="comment-49041" class="comment">
<div id="post-49041-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Apparently my assumption that the date alone is sufficient is incorrect. Using date:"2015-01-01T06:55:00Z" omits the banks created yesterday, the date alone includes them.</p>
</div>
<div id="comment-49041-info" class="comment-info">
<span class="comment-age">(05 Apr '16, 15:15)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="49046"></span>
<div id="comment-49046" class="comment not_top_scorer">
<div id="post-49046-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, adding an hour seems to filter the list a bit. But still, it returns seemingly odd data. For example I get that node 2147630318 that originates from this changeset 14966325 that is closed at 2013-02-09. How exactly does the <code>date</code> parameter works in Overpass API? Is it documented somewhere?</p>
</div>
<div id="comment-49046-info" class="comment-info">
<span class="comment-age">(05 Apr '16, 16:32)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="49047"></span>
<div id="comment-49047" class="comment not_top_scorer">
<div id="post-49047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> I've got a lot of highlights from that query, not just 3 things. And I really see those were returned in the Data tab. Adding hour and time to the query seems to filter the query to those 3 items you see. It is curious why did the same query returned different data for you and for me.</p>
</div>
<div id="comment-49047-info" class="comment-info">
<span class="comment-age">(05 Apr '16, 16:35)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="49048"></span>
<div id="comment-49048" class="comment">
<div id="post-49048-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's documented at the link above. Beyond that, the source code.</p>
<p>Showing something from 2013 matches my expectations, the date query shows the results of querying the OSM database as it existed on the date in question. Use diff/adiff to see the changes that occurred over a chosen period of time.</p>
</div>
<div id="comment-49048-info" class="comment-info">
<span class="comment-age">(05 Apr '16, 16:51)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-49027" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-49027-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49022"></span>

<div id="answer-container-49022" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49022-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can find the changeset where you added the data in your edit history you can click on one of the items you added to see the current version, and from there the history for that node, to work out what happened to it when.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '16, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-49022" class="comments-container">
<span id="49045"></span>
<div id="comment-49045" class="comment">
<div id="post-49045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That would be hard, due to the large number of my changesets, and me not knowing when exactly did I added those amenities...</p>
</div>
<div id="comment-49045-info" class="comment-info">
<span class="comment-age">(05 Apr '16, 16:26)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
</div>
<div id="comment-tools-49022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49022-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49025"></span>

<div id="answer-container-49025" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49025-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are ways to only see local edits, see <a href="/questions/7/">how-do-i-see-the-history-for-my-area</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '16, 19:32</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-49025" class="comments-container">
&#10;</div>
<div id="comment-tools-49025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49025-form-container" class="comment-form-container">
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

