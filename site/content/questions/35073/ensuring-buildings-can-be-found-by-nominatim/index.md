+++
type = "question"
title = "Ensuring buildings can be found by Nominatim"
description = '''I have been adding lots of stuff to the map lately and for some reason none of them are findable. For example, searching the search box on the main OSM page to search for: &quot;Tower B, 555 Legget Dr, Ottawa&quot; Returns no results. Searching for &quot;555 Legget Dr, Ottawa&quot; Returns  House 555, Legget Drive, Mor...'''
date = "2014-07-21T22:42:00Z"
lastmod = "2014-08-14T08:06:00Z"
weight = 35073
keywords = [ "search", "nominatim" ]
aliases = [ "/questions/35073" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ensuring buildings can be found by Nominatim](/questions/35073/ensuring-buildings-can-be-found-by-nominatim)

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
<span id="post-35073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35073-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been adding lots of stuff to the map lately and for some reason none of them are findable.</p>
<p>For example, searching the search box on the main OSM page to search for:</p>
<p>"Tower B, 555 Legget Dr, Ottawa"</p>
<p>Returns no results.</p>
<p><a href="https://www.openstreetmap.org/search?query=555%20Legget%20Drive%2C%20Ottawa#map=19/45.34884/-75.91911">Searching for "555 Legget Dr, Ottawa"</a></p>
<p>Returns</p>
<ul>
<li>House 555, Legget Drive, Morgan's Grant, Ottawa, Ontario, K2K 2X3, Canada</li>
<li>House <a href="https://www.openstreetmap.org/way/293306736">Tower B, 555, Legget Drive, Morgan's Grant, Ottawa, Ontario, K2K 2X3, Canada</a></li>
<li>House <a href="https://www.openstreetmap.org/way/293306734">Tower A, 555, Legget Drive, Morgan's Grant, Ottawa, Ontario, K2K 2X3, Canada</a></li>
<li>Company CSC, 555, Legget Drive, Morgan's Grant, Ottawa, Ontario, K2K 2X3, Canada</li>
</ul>
<p>Why does Nominatim not see these Tower A/B buildings when I search for them?</p>
<p>What should I be doing to ensure that buildings/areas/features I add in the future are picked up by Nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '14, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a8460f1891830c4cfdfb6707d8cb56ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikewilliamson&#39;s gravatar image" />
<p><span>mikewilliamson</span><br />
<span class="score" title="81 reputation points">81</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikewilliamson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35073" class="comments-container">
&#10;</div>
<div id="comment-tools-35073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35073-form-container" class="comment-form-container">
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

<span id="35079"></span>

<div id="answer-container-35079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35079-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This seems to be a Nominatim bug. It works if you omit the house number, i.e. <a href="https://www.openstreetmap.org/search?query=Tower%20BB%2C%20BLegget%20BDr%2C%20BOttawa">searching for "Tower B, Legget Dr, Ottawa"</a>.</p>
<p>Other addresses have the same issue. Searching for the house number works, searching for the name works, but searching for the name <em>and</em> the house number doesn't. I created a <a href="https://github.com/twain47/Nominatim/issues/164">ticket</a> for this issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '14, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '14, 10:22</strong> </span></p>
</div>
</div>
<div id="comments-container-35079" class="comments-container">
<span id="35114"></span>
<div id="comment-35114" class="comment">
<div id="post-35114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any advice for tagging or organizing these objects that help Nominatim do its job?</p>
</div>
<div id="comment-35114-info" class="comment-info">
<span class="comment-age">(23 Jul '14, 19:13)</span> <span class="comment-user userinfo">mikewilliamson</span>
</div>
</div>
<span id="35115"></span>
<div id="comment-35115" class="comment">
<div id="post-35115-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The tagging seems to be correct. Let's wait for the Nominatim maintainers to comment on the ticket.</p>
</div>
<div id="comment-35115-info" class="comment-info">
<span class="comment-age">(23 Jul '14, 19:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="35606"></span>
<div id="comment-35606" class="comment">
<div id="post-35606-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you elaborate on what constitutes "correct" tagging? I have tried adding many other buildings/areas/etc and nominatim can't find any of them. I just happened to give you an example with a bug. I tried using the "is_in" tag on the Mindspace technology park in Hyderabad, but Nominatim can only find the bus stop across the street: <a href="http://www.openstreetmap.org/node/655159152#map=19/17.44100/78.37798">http://www.openstreetmap.org/node/655159152#map=19/17.44100/78.37798</a></p>
</div>
<div id="comment-35606-info" class="comment-info">
<span class="comment-age">(07 Aug '14, 07:29)</span> <span class="comment-user userinfo">mikewilliamson</span>
</div>
</div>
<span id="35694"></span>
<div id="comment-35694" class="comment">
<div id="post-35694-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you a little bit more specific which objects Nominatim can't find and which search keywoards you are using? Searching for <a href="http://nominatim.openstreetmap.org/search.php?q=Building+9%2C+Hitech+City">Building 9, Hitech Ciy</a> works for example. If you open the <a href="http://nominatim.openstreetmap.org/details.php?place_id=9195428311">search result</a> you can also take a look at the address hierarchy calculated by Nominatim. Furthermore instead of the <em>is_in</em> tag(s) you should try to add proper <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">administrative boundaries</a> and Nominatim will be much more happy.</p>
</div>
<div id="comment-35694-info" class="comment-info">
<span class="comment-age">(11 Aug '14, 09:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="35794"></span>
<div id="comment-35794" class="comment">
<div id="post-35794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's actually a good example. Building 9 is in a technology park named Mindspace. Mindspace is part of an area in the city of Hyderabad named "HITEC City" (but every possible variation of spelling is used). The proper name does not work: "Building 9, HITEC City" neither does "Building 9, Mindspace Technology Park" or "Building 9, Mindspace". "Hitech City" city is a single point of name="Hightech City" not to far away, while building 9 is surrounded by a landuse=commercial area with name="Mindspace Technology Park" and Nominatim can't find it at all. "Mindspace, Hyderabad" barely gets works.</p>
</div>
<div id="comment-35794-info" class="comment-info">
<span class="comment-age">(13 Aug '14, 22:01)</span> <span class="comment-user userinfo">mikewilliamson</span>
</div>
</div>
<span id="35810"></span>
<div id="comment-35810" class="comment not_top_scorer">
<div id="post-35810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess Nominatim ignores <em>landuse</em> for address lookups. This might be intentional because they are usually not part of the address or it is just a shortcoming at the moment. Searching for "Building 9, HITEC City" won't work because the proper name seems to be "HITECH City" (including the <em>H</em>) and Nominatim is currently not able to correct spelling mistakes. However you can try to add an <a href="https://wiki.openstreetmap.org/wiki/Key:name">alt_name</a> to the <a href="http://www.openstreetmap.org/node/2926946739">suburb node</a>. But only if this alternative name is really in use, <em>alt_name</em> should not be used to correct spelling mistakes. Everything else has to be answered by one of the Nominatim developers which sometimes show up on help but apparently didn't looked at this question so far.</p>
</div>
<div id="comment-35810-info" class="comment-info">
<span class="comment-age">(14 Aug '14, 08:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35079" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-35079-form-container" class="comment-form-container">
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

