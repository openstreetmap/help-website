+++
type = "question"
title = "How can I get Overpass-API to just display my objects with just one tag ?"
description = '''Hey, you can I ask Overpass to just give me back Objects with just one particular tag and no other tags. e.g. if a object has the tag building=yes it should be displayed if it has building=yes and addr:city=whatever it shouldn&#x27;t? How can i make that happen ? Thanks for your answers!'''
date = "2013-06-03T20:05:00Z"
lastmod = "2017-08-29T08:58:00Z"
weight = 22996
keywords = [ "overpass", "tag", "osm" ]
aliases = [ "/questions/22996" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get Overpass-API to just display my objects with just one tag ?](/questions/22996/how-can-i-get-overpass-api-to-just-display-my-objects-with-just-one-tag)

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
<span id="post-22996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22996-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, you can I ask Overpass to just give me back Objects with <strong>just one</strong> particular tag and no other tags. e.g. if a object has the tag building=yes it should be displayed if it has building=yes and addr:city=whatever it shouldn't?</p>
<p>How can i make that happen ? Thanks for your answers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '13, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0c43c2c53ad9723aa6598d37579b2bbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hno2&#39;s gravatar image" />
<p><span>hno2</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hno2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22996" class="comments-container">
<span id="36726"></span>
<div id="comment-36726" class="comment">
<div id="post-36726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Update September 2014: Now that Overpass API also supports regular expressions for keys, this kind of query is now possible. See my answer below for details.</p>
</div>
<div id="comment-36726-info" class="comment-info">
<span class="comment-age">(10 Sep '14, 10:12)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-22996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22996-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="23001"></span>

<div id="answer-container-23001" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23001-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if overpass API can count tags. Neither do I know if you can query "your" objects.</p>
<p>If you are looking for buildings wighout house numbers, you could either use <a href="http://qa.poole.ch/?layers=FTFB0">Simon's no address layer</a> or you could use <a href="http://overpass-turbo.eu/s/i3">this overpass query</a> (objects that have a building tag set and don't have an addr:housenumber tag):</p>
<pre><code>(
 node({{bbox}})[&quot;building&quot;]
  [&quot;addr:housenumber&quot;!~&quot;.*&quot;];
 way({{bbox}})[&quot;building&quot;]
  [&quot;addr:housenumber&quot;!~&quot;.*&quot;];
 rel({{bbox}})[&quot;building&quot;]
  [&quot;addr:housenumber&quot;!~&quot;.*&quot;];
);
(._;&gt;;);
out;</code></pre>
<p>HTH /al</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '13, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-23001" class="comments-container">
<span id="27085"></span>
<div id="comment-27085" class="comment">
<div id="post-27085-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, I was looking for a query to find ways with addr:interpolation but without addr:street</p>
<pre><code>(
 node({{bbox}})[&quot;addr:interpolation&quot;]
  [&quot;addr:street&quot;!~&quot;.*&quot;];
 way({{bbox}})[&quot;addr:interpolation&quot;]
  [&quot;addr:street&quot;!~&quot;.*&quot;];
 rel({{bbox}})[&quot;addr:interpolation&quot;]
  [&quot;addr:street&quot;!~&quot;.*&quot;];
);
(._;&gt;;);
out;</code></pre>
</div>
<div id="comment-27085-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 20:17)</span> <span class="comment-user userinfo">cyph3r</span>
</div>
</div>
<span id="41849"></span>
<div id="comment-41849" class="comment">
<div id="post-41849-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Overpass API cannot count tags yet. There's an open issue for that on Github: <a href="https://github.com/drolbr/Overpass-API/issues/197">https://github.com/drolbr/Overpass-API/issues/197</a></p>
</div>
<div id="comment-41849-info" class="comment-info">
<span class="comment-age">(22 Mar '15, 17:07)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-23001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23001-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36725"></span>

<div id="answer-container-36725" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36725-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A combination of the difference operator and regular expressions for keys can make this happen. Unfortunately, you cannot use negative look-ahead (?!) for regular expressions, which makes the whole story very complex (see <a href="http://stackoverflow.com/questions/7883819/using-posix-to-exclude-a-word-inside-a-string">this stackoverflow post</a> on how to build such an expression).</p>
<p>That's why I resort to a simplified approach and exclude buildings, which have any tags that don't start with a letter "b". However, the basic principle is the same.</p>
<pre><code>[bbox:{{bbox}}];
((
// retrieve all buildings    
  way[building=yes];
// and remove...    
  - 
// all buildings which also have a tag not starting with &quot;b&quot;    
  way[building=yes][~&quot;^[^b].*$&quot;~&quot;.&quot;]; 
); &gt;; );
out;</code></pre>
<p>Try in Overpass Turbo: <a href="http://overpass-turbo.eu/s/4Z9">http://overpass-turbo.eu/s/4Z9</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '14, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-36725" class="comments-container">
&#10;</div>
<div id="comment-tools-36725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36725-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="58855"></span>

<div id="answer-container-58855" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58855-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/rjM">http://overpass-turbo.eu/s/rjM</a> has an example of query that is using tag counting. It will find poorly tagged object - with only tourism=attraction or tourism attraction + name tag in Poland,</p>
<pre><code>/*
This has been generated by the overpass-turbo wizard.
The original search was:
“addr:housenumber=* and name=* and type:node and aeroway!=* and amenity!=* and craft!=* and historic!=* and leisure!=* and man_made!=* and office!=* and power!=* and railway!=* and shop!=* and tourism!=* in Polska”
*/
[out:xml]/*fixed by auto repair*/[timeout:2500];
// fetch area “Polska” to search in
{{geocodeArea:Polska}}-&gt;.searchArea;
// gather results
(
  // query part for: “&quot;addr:housenumber&quot;=* and name=* and aeroway!=* and amenity!=* and craft!=* and historic!=* and leisure!=* and man_made!=* and office!=* and power!=* and railway!=* and shop!=* and tourism!=*”
 node[tourism=attraction](if:count_tags()==1)(area.searchArea);
   node[tourism=attraction][name](if:count_tags()==2)(area.searchArea);
);
// print results
out meta;/*fixed by auto repair*/
&gt;;
out meta qt;/*fixed by auto repair*/</code></pre>
<p>query was provided by RicoElectrico, thanks! source: <a href="https://forum.openstreetmap.org/viewtopic.php?pid=661266#p661266">https://forum.openstreetmap.org/viewtopic.php?pid=661266#p661266</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '17, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/220a7c896723cbc2b5d57a1bfd5d66f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mateusz%20Konieczny&#39;s gravatar image" />
<p><span>Mateusz Koni...</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mateusz Konieczny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '17, 08:59</strong> </span></p>
</div>
</div>
<div id="comments-container-58855" class="comments-container">
&#10;</div>
<div id="comment-tools-58855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58855-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23019"></span>

<div id="answer-container-23019" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23019-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-23019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure what you mean.</p>
<p>Concerning the output format, Overpass API prints for an object always either all tags or no tags at all.</p>
<p>If you want to find an object with a certain tag but not a certain other tag, you can the solution provided by _al above.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '13, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-23019" class="comments-container">
<span id="23021"></span>
<div id="comment-23021" class="comment">
<div id="post-23021-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As far as I understand he is looking for a solution to find objects which only have one tag - the specified tag - and no other tags at all.</p>
</div>
<div id="comment-23021-info" class="comment-info">
<span class="comment-age">(05 Jun '13, 08:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="23035"></span>
<div id="comment-23035" class="comment">
<div id="post-23035-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thats right, e.g a node with the tag addr:street: Obama Alley and without any other tags should be printed a node with addr:street and addr:country not. But I already solved my problem with an other possible solution</p>
</div>
<div id="comment-23035-info" class="comment-info">
<span class="comment-age">(05 Jun '13, 16:45)</span> <span class="comment-user userinfo">hno2</span>
</div>
</div>
</div>
<div id="comment-tools-23019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23019-form-container" class="comment-form-container">
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

