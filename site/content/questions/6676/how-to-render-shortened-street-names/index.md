+++
type = "question"
title = "How to render shortened street names?"
description = '''Short question: How do I inform OSM renderers that some common streetname words should be abbreviated? Long question: This maybe a question about Mapnik, but it can be useful for contributors from non-English speaking countries. It seems reasonable that streetnames in OpenStreetMap should be always ...'''
date = "2011-07-28T19:36:00Z"
lastmod = "2019-11-08T21:27:00Z"
weight = 6676
keywords = [ "rendering", "search", "geocoding", "streetnames", "mapnik" ]
aliases = [ "/questions/6676" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to render shortened street names?](/questions/6676/how-to-render-shortened-street-names)

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
<span id="post-6676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6676-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-6676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Short question:</strong></p>
<p>How do I inform OSM renderers that some common streetname words should be abbreviated?</p>
<p><strong>Long question:</strong></p>
<p>This maybe a question about Mapnik, but it can be useful for contributors from non-English speaking countries.</p>
<p>It seems reasonable that streetnames in OpenStreetMap should be always in their unabbreviated versions, with very few exceptions. This is better for searching/geocoding and avoiding duplicates.</p>
<p>But maps can be cluttered while rendering long streetnames in certain areas, so my question is, how can I inform Mapnik or other renderers used by OpenStreetMap that a streetname started with "Avenida" should be rendered as "Av."?</p>
<p>These are examples from my country, Brazil, but I'm sure mappers from other parts of the world have the same problem:</p>
<p>"Avenida Doutor Ricardo Jafet" =&gt; "Av. Dr. Ricardo Jafet"</p>
<p>"Rua Professor Roberto Hottinger" =&gt; "R. Prof. Roberto Hottinger"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '11, 19:36</strong></p>
<img src="https://secure.gravatar.com/avatar/77ac2d599553a2b1a968b473d4bf670b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vgeorge&#39;s gravatar image" />
<p><span>vgeorge</span><br />
<span class="score" title="201 reputation points">201</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vgeorge has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6676" class="comments-container">
<span id="6690"></span>
<div id="comment-6690" class="comment">
<div id="post-6690-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>in Potlatch 2, in the "naming" tab, you have an "alternative name" field: search for its use, maybe it can convey what you need?</p>
</div>
<div id="comment-6690-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 10:52)</span> <span class="comment-user userinfo">Herve5</span>
</div>
</div>
<span id="6701"></span>
<div id="comment-6701" class="comment">
<div id="post-6701-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think this tag is more suitable for completely different names, and it is more efficient to have renderers and geocoders to handle country-specific abbreviations.</p>
</div>
<div id="comment-6701-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 18:42)</span> <span class="comment-user userinfo">vgeorge</span>
</div>
</div>
<span id="12993"></span>
<div id="comment-12993" class="comment">
<div id="post-12993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>adding tags for alternate names (in the same language specified by the language suffix) is certainly the best solution for the general case. Renderers will then select the longest name that fit in their rendering style. But renderers may also automatically recognize some common words that can be abbreviated, provided the language code is specified, and knowing the linguistic rules about how peoples are named (this allows abbreviating known first names, keeping the last name that occurs most often after the first name in most languages). In case of ambiguity, the other translations may help.</p>
</div>
<div id="comment-12993-info" class="comment-info">
<span class="comment-age">(28 May '12, 07:22)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
</div>
<div id="comment-tools-6676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6676-form-container" class="comment-form-container">
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

<span id="6678"></span>

<div id="answer-container-6678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6678-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is actually a list of common abbreviations for various languages used by Name Finder and Nominatim: <a href="http://wiki.openstreetmap.org/wiki/Name_finder:Abbreviations">http://wiki.openstreetmap.org/wiki/Name_finder:Abbreviations</a></p>
<p>I can't speak for Mapnik, but as the developer of <a href="http://maperitive.net">Maperitive</a>, I intend to add support for user-defined abbreviations in Maperitive in the near future.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '11, 20:33</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-6678" class="comments-container">
<span id="6697"></span>
<div id="comment-6697" class="comment">
<div id="post-6697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For anyone looking at doing anything like this, I added a comment to the potlatch2 enhancement request aimed at doing the reverse: <a href="http://trac.openstreetmap.org/ticket/3432">http://trac.openstreetmap.org/ticket/3432</a></p>
<p>It obviously can be done, but it's difficult and requires a lot of thought. At the organisation I work for, we decided it was too risky because of what we are doing with the data.</p>
</div>
<div id="comment-6697-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 17:48)</span> <span class="comment-user userinfo">c2r</span>
</div>
</div>
<span id="6700"></span>
<div id="comment-6700" class="comment">
<div id="post-6700-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>c2r: This is very country specific, but seems a good idea. It would be useful to have a plugin in JOSM for that.</p>
<p>Breki: I've asked in the talk-page for Nominatim in wiki about this six months ago and no one aswered, so it seems that it's not the right communication channel with the developers. I have no problem in coding this myself, but I can't find instructions to do so.</p>
</div>
<div id="comment-6700-info" class="comment-info">
<span class="comment-age">(29 Jul '11, 18:40)</span> <span class="comment-user userinfo">vgeorge</span>
</div>
</div>
<span id="12994"></span>
<div id="comment-12994" class="comment">
<div id="post-12994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Automatically generating abbreviations or deciphering abbreviations into full words is horribly complicated and can easily fall into stupidities. For these reasons, acceptable abbreviations should better be part of tags. But as "alt_name:*" are used for completely different alternate names.</p>
</div>
<div id="comment-12994-info" class="comment-info">
<span class="comment-age">(28 May '12, 07:32)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="12995"></span>
<div id="comment-12995" class="comment">
<div id="post-12995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would suggest adding variants like equivalent abbreviations by appending a numeric suffix to the key, e.g. "name:2"="value of name abbreviated", "name:fr:2"="valeur de name:fr abrégée". The numeric suffix can grow if the name is more abreviated and several levels of abbreviations are used. The standard key for each language or for the default language (without the language code) should be the full unabbreviated name.</p>
</div>
<div id="comment-12995-info" class="comment-info">
<span class="comment-age">(28 May '12, 07:32)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="12996"></span>
<div id="comment-12996" class="comment">
<div id="post-12996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note however that some places have used the key "short_name" for abbreviations. We may also avoid multiple keys for several levels by using a list of values separated by semicolons. Another idea could be to set a key like "name:suffix:en=Street", "name:prefix:fr=Rue", to indicate which parts of the name is an abbreviatable prefix or suffix in the full street name given in key "name:<em>", or the opposite by indicating the key "name:main:</em>" to indicate which part in "name:*" should NOT be abreviated (the rest being resolved according to generic rules for each language)</p>
</div>
<div id="comment-12996-info" class="comment-info">
<span class="comment-age">(28 May '12, 07:39)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="17933"></span>
<div id="comment-17933" class="comment not_top_scorer">
<div id="post-17933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know, that this can be implemented independently in different rendering engines, but the majority of users will probably still use mapnik/osm.org. Personally I would <em>love</em> to have a button [Abbreviate names] on osm.org next to the layers widget! :)</p>
<p><span>@Verdy_p</span>: Generating full names from abbreviations is certainly tricky. But abbreviating "Street" to "St." (and others: osm.org/wiki/Name_finder:Abbreviations) should be quite easy since we probably know the correct language either from the coordinates or the (name:en=*) tag. But maybe I'm missing something here. [See below...]</p>
<p>If the abbreviation can be obviously generated from the name without any doubt (as in East Street) then there is probably no point in adding complexity to the tagging scheme. Only if the automatic abbreviation is likely to fail ('Thomas Street' Square &gt; 'Thomas St.' Sq.) then a more complex tagging makes sense.</p>
</div>
<div id="comment-17933-info" class="comment-info">
<span class="comment-age">(23 Nov '12, 18:08)</span> <span class="comment-user userinfo">Zeptomoon</span>
</div>
</div>
</div>
<div id="comment-tools-6678" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-6678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17934"></span>

<div id="answer-container-17934" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17934-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the case of Mapquest, they already do this for the USA (have a look <a href="http://www.openstreetmap.org/?lat=37.45939&amp;lon=-122.43269&amp;zoom=15&amp;layers=Q">here</a> for an example). You could try and influence them to do the same (with presumably different abbreviations) for your country too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '12, 18:25</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17934" class="comments-container">
&#10;</div>
<div id="comment-tools-17934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17934-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71544"></span>

<div id="answer-container-71544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71544-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-71544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Shortened names should IMHO be in <code>short_name</code> tag, possibly with several values. This way the rendered does not need to make up an abbreviation itself, following numerous national conventions, but rather select one of the predefined ones.</p>
<p>Example</p>
<pre><code>name=Střední odborná škola civilního letectví
official_name=Střední odborná škola civilního letectví, Praha - Ruzyně 
short_name=SOŠCL Praha-Ruzyně;SOŠCL Pha-Ruz.</code></pre>
<p>I can imagine that renderer decides what is the longest text which can fit in the label (in particular context) and than select longest form from name / short_name which fits in there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '19, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e6dd88ec54643689069f97f0d52398ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gorn&#39;s gravatar image" />
<p><span>gorn</span><br />
<span class="score" title="542 reputation points">542</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gorn has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '19, 20:35</strong> </span></p>
</div>
</div>
<div id="comments-container-71544" class="comments-container">
<span id="71547"></span>
<div id="comment-71547" class="comment">
<div id="post-71547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Different renderers want to abbreviate differently in different situations. I find it difficult to ask the mapper to cater for all different needs by putting a list of possible short names on an object.</p>
</div>
<div id="comment-71547-info" class="comment-info">
<span class="comment-age">(08 Nov '19, 21:27)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71544-form-container" class="comment-form-container">
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

