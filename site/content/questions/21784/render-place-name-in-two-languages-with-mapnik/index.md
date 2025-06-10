+++
type = "question"
title = "render place name in two languages with mapnik"
description = '''Hi All, Is it possible to render place names (areas, river, streets, etc.) with two languages: place name in local language and its English translation near? Thank you.'''
date = "2013-04-24T14:57:00Z"
lastmod = "2013-04-26T13:38:00Z"
weight = 21784
keywords = [ "rendering", "mapnik", "placenames" ]
aliases = [ "/questions/21784" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [render place name in two languages with mapnik](/questions/21784/render-place-name-in-two-languages-with-mapnik)

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
<span id="post-21784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21784-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>Is it possible to render place names (areas, river, streets, etc.) with two languages: place name in local language and its English translation near?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-placenames" rel="tag" title="see questions tagged &#39;placenames&#39;">placenames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '13, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/23c04d8569cab5c5dbc443ea3a2c837e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jvalcenko&#39;s gravatar image" />
<p><span>jvalcenko</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jvalcenko has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Sep '13, 18:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-21784" class="comments-container">
&#10;</div>
<div id="comment-tools-21784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21784-form-container" class="comment-form-container">
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

<span id="21786"></span>

<div id="answer-container-21786" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21786-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-21786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jvalcenko has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes. You can see the MapQuest rendering already does something like this: <a href="http://osm.org/go/0t2tSf--?layers=Q">http://osm.org/go/0t2tSf--?layers=Q</a></p>
<p>For your own rendering, the best way to do this is likely in your PostgreSQL query. There you can add some logic to make sure all of the labels make sense, such as not including the English translation if it is the same as the local name. You'll need to make sure you have imported the <code>name:en</code> column as well as the local name. (If you are using osm2pgsql you will need to adjust your <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql#Import_style">import style</a>, or you can use hstore to import all tags, option <code>-k</code> (or <code>--hstore</code>), which obviates the need to change the default style.)</p>
<p>Here is an example query from an osm2pgsql import for a places layer. If there is a <code>name:en</code> tag for a place that is different from the <code>name</code> tag, the name will look like "Local Name (English Name)", otherwise you will just get "Local Name".</p>
<pre><code>( select way,
    case when &quot;name:en&quot; is not null and &quot;name:en&quot; &lt;&gt; name
      then name || &#39; (&#39; || &quot;name:en&quot; || &#39;)&#39;
      else name end as name
  from planet_osm_point
  where place in (&#39;city&#39;, &#39;town&#39;, &#39;village&#39;, &#39;hamlet&#39;)
) as places</code></pre>
<p>When using the hstore option replace <code>"name:en"</code> with <code>tags-&gt;'name:en'</code>.</p>
<p>A simple approach is to import into PostGIS using alternative table names, using the <code>-p</code> option, and then create views with the standard Mapnik stylesheet names. The easiest way to build the view is to query all the column names (<code>select column_name from information_schema.columns where table_name ='TAB_NAME'</code>) and use this as the basis for creating the view. Only the name column needs to be changed as shown above. (An untested example is <a href="http://pastebin.com/E8jWVcsn">here</a> on pastebin)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '13, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/90af4b163a309869d590111d8114836a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajashton&#39;s gravatar image" />
<p><span>ajashton</span><br />
<span class="score" title="170 reputation points">170</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajashton has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Sep '13, 10:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-21786" class="comments-container">
&#10;</div>
<div id="comment-tools-21786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21786-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21882"></span>

<div id="answer-container-21882" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21882-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Like in <a href="http://osm-tools.org/">http://osm-tools.org</a> -&gt; thaimap ?</p>
<p>Ask the maintainer of that site: scroll down the page to see contact data. Or read his explanation how he did that.</p>
<p>Also see <a href="http://wiki.openstreetmap.org/wiki/Map_internationalization">Map_internationalization</a> in general.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '13, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-21882" class="comments-container">
&#10;</div>
<div id="comment-tools-21882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21882-form-container" class="comment-form-container">
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

