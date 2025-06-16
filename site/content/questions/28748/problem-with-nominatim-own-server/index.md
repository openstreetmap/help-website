+++
type = "question"
title = "Problem with nominatim own server"
description = '''I&#x27;ve downloaded the osm virtual machine here: https://wiki.openstreetmap.org/wiki/Virtual_machine_image ...and patched the local.php file (for the &quot;declaration allowed only at the start of the document&quot; error). It appears to be working fine, except for the following issue: I understand there are two ...'''
date = "2013-12-04T06:04:00Z"
lastmod = "2013-12-04T18:02:00Z"
weight = 28748
keywords = [ "private_server", "results" ]
aliases = [ "/questions/28748" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with nominatim own server](/questions/28748/problem-with-nominatim-own-server)

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
<span id="post-28748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28748-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've downloaded the osm virtual machine here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Virtual_machine_image">https://wiki.openstreetmap.org/wiki/Virtual_machine_image</a></p>
<p>...and patched the local.php file (for the "declaration allowed only at the start of the document" error). It appears to be working fine, except for the following issue:</p>
<p>I understand there are two ways to query for an address:</p>
<pre><code> q=&lt;query&gt;
   Query string to search for.  Alternatively can be entered as:</code></pre>
<p>and</p>
<pre><code> street=&lt;housenumber&gt; &lt;streetname&gt;
 city=&lt;city&gt;
 county=&lt;county&gt;
 state=&lt;state&gt;
 country=&lt;country&gt;
 postalcode=&lt;postalcode&gt;
   (experimental) Alternative query string format for structured requests. 
   Structured requests are faster and require less server resources. 
   DO NOT COMBINE WITH q=&lt;query&gt; PARAMETER.</code></pre>
<p>However, the first way works, and the second one gets me no results. I thought it could be a problem with the address formatting but if I use the same query on the public nominatim server (instead of my own) I get results.</p>
<p>Check the public server output:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; ?&gt;
&lt;searchresults timestamp=&#39;Wed, 04 Dec 13 05:50:52 +0000&#39; attribution=&#39;Data ?? OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright&#39; querystring=&#39;andes 1479, montevideo, montevideo, uruguay&#39; polygon=&#39;false&#39; exclude_place_ids=&#39;96424832,57980898,70445266&#39; more_url=&#39;http://nominatim.openstreetmap.org/search?format=xml&amp;amp;exclude_place_ids=96424832,57980898,70445266&amp;amp;q=andes+1479%2C+montevideo%2C+montevideo%2C+uruguay&#39;&gt;
&lt;place place_id=&#39;96424832&#39; osm_type=&#39;way&#39; osm_id=&#39;179061638&#39; place_rank=&#39;26&#39; boundingbox=&quot;-34.9064064025879,-34.9008026123047,-56.1986999511719,-56.1981239318848&quot; lat=&#39;-34.9035605&#39; lon=&#39;-56.1984301&#39; display_name=&#39;Andes, Ciudad Vieja, Montevideo, 11100, Uruguay&#39; class=&#39;highway&#39; type=&#39;residential&#39; importance=&#39;0.9&#39;/&gt;&lt;place place_id=&#39;57980898&#39; osm_type=&#39;way&#39; osm_id=&#39;78105349&#39; place_rank=&#39;26&#39; boundingbox=&quot;-34.9114799499512,-34.9064025878906,-56.198127746582,-56.1972122192383&quot; lat=&#39;-34.9092104&#39; lon=&#39;-56.1978327&#39; display_name=&#39;Andes, Barrio Sur, Montevideo, 11100, Uruguay&#39; class=&#39;highway&#39; type=&#39;residential&#39; importance=&#39;0.9&#39;/&gt;&lt;place place_id=&#39;70445266&#39; osm_type=&#39;way&#39; osm_id=&#39;112698692&#39; place_rank=&#39;26&#39; boundingbox=&quot;-34.8365058898926,-34.8350563049316,-55.9612350463867,-55.9585113525391&quot; lat=&#39;-34.8357171&#39; lon=&#39;-55.9597648&#39; display_name=&#39;Andes, Solymar, Ciudad de la Costa, Canelones, Uruguay&#39; class=&#39;highway&#39; type=&#39;residential&#39; importance=&#39;0.7&#39;/&gt;&lt;/searchresults&gt;</code></pre>
<p>and my local server output:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; ?&gt;
&lt;searchresults timestamp=&#39;Wed, 04 Dec 13 05:50:59 +0000&#39; attribution=&#39;Data ?? OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright&#39; querystring=&#39;&#39; polygon=&#39;false&#39; more_url=&#39;http://localhost/nominatim/search?format=xml&amp;amp;exclude_place_ids=&amp;amp;accept-language=&amp;amp;q=&#39;&gt;
&lt;/searchresults&gt;</code></pre>
<p>In both cases, I'm using the same query:</p>
<pre><code>http://&lt;public server or private server&gt;/search?format=xml&amp;street=andes+1479&amp;city=montevideo&amp;county=&amp;state=montevideo&amp;country=uruguay&amp;postalcode=</code></pre>
<p>I don't know if it has something to do; but the virtual server need some minor "corrections" (?); one if to edit the local.php file (I did it) but the other one, downloading and replacing the get-coastlines.sh file, can't did it (can't overwrite existing file, and I don't have root password)</p>
<p>I appreciate any help! Regards!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-private_server" rel="tag" title="see questions tagged &#39;private_server&#39;">private_server</span> <span class="post-tag tag-link-results" rel="tag" title="see questions tagged &#39;results&#39;">results</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '13, 06:04</strong></p>
<img src="https://secure.gravatar.com/avatar/3875f3961eb0b69618914bf29ab6ef45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leos79&#39;s gravatar image" />
<p><span>leos79</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leos79 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28748" class="comments-container">
&#10;</div>
<div id="comment-tools-28748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28748-form-container" class="comment-form-container">
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

<span id="28750"></span>

<div id="answer-container-28750" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28750-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="leos79 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This virtual image is from the end of 2012 and contains a Nominatim version that is neither capable of handling <a href="https://wiki.openstreetmap.org/wiki/64-bit_Identifiers">64-bit node IDs</a> nor supports the structured search that you're attempting. The <a href="https://wiki.openstreetmap.org/wiki/Virtual_machine_image">virtual image wiki page</a> also contains a big red warning message at the beginning which you seem to have missed somehow.</p>
<p>This means that the current virtual image is of little use. Newer versions of Nominatim can handle 64-bit node IDs but this would require you to update the Nominatim version contained in the virtual image (and possible other software, too), the wiki also contains <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">Nominatim installation instructions</a>.</p>
<p>And if you really need a root password (<code>sudo</code> should be enough for everything) then you can set/change it via <code>sudo passwd</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '13, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '13, 08:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-28750" class="comments-container">
<span id="28780"></span>
<div id="comment-28780" class="comment">
<div id="post-28780-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks scai for your answer! So, this one is the last virtual server available? I'll try to make one of my own. And the root thing would be for replacing a file; I got a mesagge saying I don't have permission to do thath and I thought it was due to user permissions. I'm not a linux guy, I'm a software developer for windows environment, the closes things I know to linux is DOS and googling-for-stuff-when-required.</p>
</div>
<div id="comment-28780-info" class="comment-info">
<span class="comment-age">(04 Dec '13, 18:00)</span> <span class="comment-user userinfo">leos79</span>
</div>
</div>
<span id="28781"></span>
<div id="comment-28781" class="comment">
<div id="post-28781-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And about the red warning; I didn't missed it. I thought if the virtual server was still there that maybe it still worked; I've decided to download it and give it a try. I didn't know the OSM data's date and neither that structured search it's a 2013 improvement (maybe it's specified somewhere; that would be what I've missed). Thank you very much, again!</p>
</div>
<div id="comment-28781-info" class="comment-info">
<span class="comment-age">(04 Dec '13, 18:02)</span> <span class="comment-user userinfo">leos79</span>
</div>
</div>
</div>
<div id="comment-tools-28750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28750-form-container" class="comment-form-container">
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

