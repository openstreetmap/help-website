+++
type = "question"
title = "search cannot find addresses on Main Street in Hingham MA (Solved see Spiekerooger&#x27;s comments)"
description = '''Search returns no results for street addresses on Main Street in Hingham MA (e.g., 14 Main Street, Hingham MA 02043). It will return results for street addresses on other streets in Hingham. I&#x27;ve stared and stared at Main Street records and addresses on other streets that can be found, but I can&#x27;t s...'''
date = "2023-08-21T16:26:00Z"
lastmod = "2023-08-25T09:36:00Z"
weight = 87717
keywords = [ "search", "street", "address" ]
aliases = [ "/questions/87717" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [search cannot find addresses on Main Street in Hingham MA (Solved see Spiekerooger's comments)](/questions/87717/search-cannot-find-addresses-on-main-street-in-hingham-ma-solved-see-spiekeroogers-comments)

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
<span id="post-87717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87717-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Search returns no results for street addresses on Main Street in Hingham MA (e.g., 14 Main Street, Hingham MA 02043). It will return results for street addresses on other streets in Hingham. I've stared and stared at Main Street records and addresses on other streets that can be found, but I can't see any difference. I'm happy to make corrections if someone can give me a hint what correction needs to be made.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '23, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/721417158afeb76856dd75e825b646e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IasonTV&#39;s gravatar image" />
<p><span>IasonTV</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IasonTV has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Aug '23, 07:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span></p>
</div>
</div>
<div id="comments-container-87717" class="comments-container">
<span id="87719"></span>
<div id="comment-87719" class="comment">
<div id="post-87719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I got this error when I searched. Error contacting nominatim.openstreetmap.org: 500</p>
</div>
<div id="comment-87719-info" class="comment-info">
<span class="comment-age">(21 Aug '23, 18:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="87723"></span>
<div id="comment-87723" class="comment">
<div id="post-87723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I'm connecting OK. I can get results when I search for other addresses in Hingham MA. It's just when I search for any address on Main Street using the the street name and number that it comes back empty.</p>
</div>
<div id="comment-87723-info" class="comment-info">
<span class="comment-age">(21 Aug '23, 22:28)</span> <span class="comment-user userinfo">IasonTV</span>
</div>
</div>
<span id="87752"></span>
<div id="comment-87752" class="comment">
<div id="post-87752-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Another problem: main street might be treated as a stop word as it occurs more than 40k times in OSM data and therefore is disregarded in a search request but I'm not in the known about the new icu tokenizer at Nominatim that might handle this differently than the old tokenizer. The threshold for a frequent term to become a stop word might be handled differently based on the actual nominatim config settings of a backend.</p>
<p>At least it's quite common that "Main Street" is a special problem for geocoders (e.g. in comparison to "Howard Smith Drive").</p>
</div>
<div id="comment-87752-info" class="comment-info">
<span class="comment-age">(24 Aug '23, 11:13)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="87753"></span>
<div id="comment-87753" class="comment">
<div id="post-87753-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thankyou for info.</p>
</div>
<div id="comment-87753-info" class="comment-info">
<span class="comment-age">(24 Aug '23, 12:33)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-87717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87717-form-container" class="comment-form-container">
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

<span id="87720"></span>

<div id="answer-container-87720" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87720-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I did a search for a house number that I added a few days ago it works ok in England. this is what I searched for:- 9 ambury road Huntingdon UK I cannot see what is wrong with the mapping data for hingham. Oddly if I add plymouth to your search it works 14 main street hingham plymouth MA We need someone with high level of skill to help us. EDIT and Update<br />
Spiekerooger thanks for your last comment and info, and letting us know the search is working now. Look at his last comment if you wish to know a little more. Thanks again. Spiekerooger AND now it works see <a href="https://www.openstreetmap.org/search?query=14%20main%20street%20hingham%20Ma#map=15/42.2416/-70.8898">https://www.openstreetmap.org/search?query=14%20main%20street%20hingham%20Ma#map=15/42.2416/-70.8898</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '23, 18:22</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '23, 09:59</strong> </span></p>
</div>
</div>
<div id="comments-container-87720" class="comments-container">
<span id="87722"></span>
<div id="comment-87722" class="comment">
<div id="post-87722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it's just the addresses on Main Street in Hingham MA USA as far as I can tell. And other streets in Hingham can be searched for. I suspect there might be something off with the street record(s) rather than the individual addresses, but I don't see anything odd there either</p>
</div>
<div id="comment-87722-info" class="comment-info">
<span class="comment-age">(21 Aug '23, 22:25)</span> <span class="comment-user userinfo">IasonTV</span>
</div>
</div>
<span id="87750"></span>
<div id="comment-87750" class="comment">
<div id="post-87750-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>lasonTV I have looked at the data, as you have, I also can't see why your example search 14 main street Hingham MA does not work. BUT I have found this does 14 main street hingham plymouth MA. HELP please we are mystified. Hopefully this comment push you question to the top again. And maybe it will get someone with a lot more knowledge who can spot the problem and tell us why.</p>
</div>
<div id="comment-87750-info" class="comment-info">
<span class="comment-age">(24 Aug '23, 08:47)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="87751"></span>
<div id="comment-87751" class="comment">
<div id="post-87751-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I do find the right building (this one: <a href="https://www.openstreetmap.org/way/213467160)">https://www.openstreetmap.org/way/213467160)</a> while searching for 14 Main Street, Hingham MA 02043 at osm.org, e.g. <a href="https://www.openstreetmap.org/search?query=14%20Main%20Street%2C%20Hingham%20MA%2002043#map=19/42.24211/-70.88871">https://www.openstreetmap.org/search?query=14%20Main%20Street%2C%20Hingham%20MA%2002043#map=19/42.24211/-70.88871</a> but not while searching at nominatim.osm.org, e.g. <a href="https://nominatim.osm.org/ui/search.html?street=14+Main+Street&amp;city=Hingham&amp;state=MA&amp;postalcode=02043">https://nominatim.osm.org/ui/search.html?street=14+Main+Street&amp;city=Hingham&amp;state=MA&amp;postalcode=02043</a> (structured) or <a href="https://nominatim.osm.org/ui/search.html?q=14+Main+Street%2C+Hingham+MA+02043">https://nominatim.osm.org/ui/search.html?q=14+Main+Street%2C+Hingham+MA+02043</a> (unstructured). This seems to be a problem with the new frontend at nominatim.osm.org. Or it could be a problem with different backends getting different results/updates. Also while using the search field at www.osmap.us (a site where I control the geocoder backend) for 14 Main Street, Hingham MA 02043 does show the right building. So it is in the osm data but there seem to be some problems with the new frontend at nominatim.osm.org that even seem to interfere with direct requests (e.g. /search.php?... instead of the ui frontend). Probably best to open an issue at <a href="https://github.com/osm-search/nominatim-ui/issues">https://github.com/osm-search/nominatim-ui/issues</a> I would assume.</p>
</div>
<div id="comment-87751-info" class="comment-info">
<span class="comment-age">(24 Aug '23, 10:54)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="87757"></span>
<div id="comment-87757" class="comment">
<div id="post-87757-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>and now the request at the Nominatim frontend (nominatim.osm.org) finds them as well. Don't know what changed there or why this hiccup happened...</p>
</div>
<div id="comment-87757-info" class="comment-info">
<span class="comment-age">(25 Aug '23, 09:36)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-87720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87720-form-container" class="comment-form-container">
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

