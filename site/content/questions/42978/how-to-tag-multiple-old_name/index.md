+++
type = "question"
title = "how to tag multiple old_name?"
description = '''Let&#x27;s say a street is known to have had name1 first, then name2, then name3. How should this be tagged so that Nominatim would be able to search in all of them? http://wiki.openstreetmap.org/wiki/Key:name suggests alt_name_1 (and so on) for alternative names, http://wiki.openstreetmap.org/wiki/Talk:...'''
date = "2015-05-09T07:44:00Z"
lastmod = "2018-03-31T15:51:00Z"
weight = 42978
keywords = [ "names", "tagging" ]
aliases = [ "/questions/42978" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to tag multiple old_name?](/questions/42978/how-to-tag-multiple-old_name)

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
<span id="post-42978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42978-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Let's say a street is known to have had name1 first, then name2, then name3. How should this be tagged so that Nominatim would be able to search in all of them?</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Key:name">http://wiki.openstreetmap.org/wiki/Key:name</a> suggests alt_name_1 (and so on) for alternative names, <a href="http://wiki.openstreetmap.org/wiki/Talk:Names#multiple_alt_names_or_loc_names.3F">http://wiki.openstreetmap.org/wiki/Talk:Names#multiple_alt_names_or_loc_names.3F</a> actually discourages that.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Key:name#Values">http://wiki.openstreetmap.org/wiki/Key:name#Values</a> also proposes a way to specify years when the name was used, but how to handle the case when the sequence of the names is known, but the exact years when each was used - not?</p>
<p>Update: To clarify why it would be useful to map old names, in many cases the name change is not that long ago. There would still be printed materials referencing the old name, and in case of more recent changes, probably hundreds of websites using the old name still. Having such information in the map is useful today as people could be easily be given the old name and searching for it.</p>
<p>Another usecase is historical features like mounds or hills. While they might have one more prominent name, in many cases there are several other names they are or were known by.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '15, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richlv has 5 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '18, 19:52</strong> </span></p>
</div>
</div>
<div id="comments-container-42978" class="comments-container">
&#10;</div>
<div id="comment-tools-42978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42978-form-container" class="comment-form-container">
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

<span id="42980"></span>

<div id="answer-container-42980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42980-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure there is actually such a need for tagging historic names, given that we want names -in use- in OSM (contrary to OHM). I would only use old_name and potentially alt_name if the names are still commonly used.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '15, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-42980" class="comments-container">
<span id="42981"></span>
<div id="comment-42981" class="comment">
<div id="post-42981-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>in some cases the old names are extensively used in old (and even not so old) documents. it would be highly useful both to have them in the osm database and have them show up in searches. "historical search" that would kep all previous names of an object in osm could solve some of that, although often we only add old name after the object has been in osm for a while. additionally, the "previous name in osm" could have easily been a typo, so we wouldn't want to include that at all. as an example, in riga there's a a street called "Zigfrīda Annas Meierovica bulvāris". it was called "Basteja bulvāris" from 1990 until 2008, and lots of documents refer to that name. overall, using osm, there is no way to distinguish actual old names from typos. as such, it is very useful to record previous names both for data itself, as well as for the posterity of osm (showing up in search results for the old names)</p>
</div>
<div id="comment-42981-info" class="comment-info">
<span class="comment-age">(09 May '15, 10:03)</span> <span class="comment-user userinfo">Richlv</span>
</div>
</div>
<span id="42982"></span>
<div id="comment-42982" class="comment">
<div id="post-42982-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Woudn't this be a classical and useful role for a wikidata link?</p>
<p>I'm on the record for saying that core OSM data should be in OSM proper and not dependent on a 3rd party, but your use case would seem to be one which fits nicely for wikidata.</p>
</div>
<div id="comment-42982-info" class="comment-info">
<span class="comment-age">(09 May '15, 10:39)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="42984"></span>
<div id="comment-42984" class="comment not_top_scorer">
<div id="post-42984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"overall, using osm, there is no way to distinguish actual old names from typos."</p>
<p>I don't get this? There is the "old_name" key just for that: putting in old names. Anything in there is considered not a 'typo'... why are you suggesting you can't use old names? Or is it just because the default Nominatim search doesn't consider "old_name" keys (I don't know whether that is the case or not, haven't tried), and you thus feel obliged to put an "old_name" in the "name" key somehow (which of course is bad habit and impossible as it is already used for current name)</p>
</div>
<div id="comment-42984-info" class="comment-info">
<span class="comment-age">(09 May '15, 11:08)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="42986"></span>
<div id="comment-42986" class="comment">
<div id="post-42986-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9580/mboeringa">@mboeringa</a> <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview#Names">http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview#Names</a></p>
</div>
<div id="comment-42986-info" class="comment-info">
<span class="comment-age">(09 May '15, 11:23)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="42988"></span>
<div id="comment-42988" class="comment">
<div id="post-42988-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>According to the page from SimonPoole's comment, you can use old_name:1=foo, old_name:2=bar and so on.</p>
</div>
<div id="comment-42988-info" class="comment-info">
<span class="comment-age">(09 May '15, 12:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42989"></span>
<div id="comment-42989" class="comment">
<div id="post-42989-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> Thanks, I hadn't seen that page before, gives some insight into Nominatim.</p>
</div>
<div id="comment-42989-info" class="comment-info">
<span class="comment-age">(09 May '15, 12:18)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="42994"></span>
<div id="comment-42994" class="comment not_top_scorer">
<div id="post-42994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> but it is unlikely that a lot of SW supports that notation (there was a longer discussion on one of the mailling lists a while back)</p>
</div>
<div id="comment-42994-info" class="comment-info">
<span class="comment-age">(09 May '15, 16:08)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="42996"></span>
<div id="comment-42996" class="comment not_top_scorer">
<div id="post-42996-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2053/simonpoole"></a><a href="http://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> Thats possibly true. But if there is currently no well-supported tag for specifying multiple *_names then we should just start establishing one. And it seems like a good idea to me to choose the tagging scheme that is supported by the geocoder running on our main map.</p>
</div>
<div id="comment-42996-info" class="comment-info">
<span class="comment-age">(09 May '15, 17:44)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42980" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-42980-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50146"></span>

<div id="answer-container-50146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I find several old names of one highway and know the years in which they where used I tag them like this:</p>
<pre><code>old_name:1939-1945
old_name:1945-1989</code></pre>
<p>This tagging is not heavily used but understandable. I agree that it isn't probably easily to parse, especially in combination with a probable additional language code – but this can be solved by coding.</p>
<p>I don't want to start to use Wikidata for this purpose. I tried it before a little and found it quite cumbersome. Additionally: Why should I divide the data which belongs to one highway into a part for OSM and one part for Wikidata?</p>
<p><img src="http://malenki.ch/d/2016-06-11_083211_scrot_taginfo_old_names_with_year_for_help.osm.org.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '16, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</img>
</div>
</div>
<div id="comments-container-50146" class="comments-container">
<span id="62876"></span>
<div id="comment-62876" class="comment">
<div id="post-62876-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>why not just <code>name:1939-1945</code>?</p>
</div>
<div id="comment-62876-info" class="comment-info">
<span class="comment-age">(31 Mar '18, 15:51)</span> <span class="comment-user userinfo">EoghanM</span>
</div>
</div>
</div>
<div id="comment-tools-50146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50146-form-container" class="comment-form-container">
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

