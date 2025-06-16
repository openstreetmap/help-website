+++
type = "question"
title = "Rendering of Chinese place names show as messy code"
description = '''I have set up the rails port on ubuntu14.04, and then I build my local tile server under the instruction of &quot;Manually building a tile server (14.04)&quot;. And I have changed the OSM map to my local tile server. I just import the beijing-china.osm.pbf data to the gis database, everything works well, but ...'''
date = "2016-08-17T05:14:00Z"
lastmod = "2016-08-17T10:25:00Z"
weight = 51467
keywords = [ "renderd", "postgres", "tileserver" ]
aliases = [ "/questions/51467" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering of Chinese place names show as messy code](/questions/51467/rendering-of-chinese-place-names-show-as-messy-code)

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
<span id="post-51467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51467-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have set up the rails port on ubuntu14.04, and then I build my local tile server under the instruction of "<a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">Manually building a tile server (14.04)</a>". And I have changed the OSM map to my local tile server. I just import the beijing-china.osm.pbf data to the gis database, everything works well, but when I view the <a href="http://localhost:3000">http://localhost:3000</a> website, I search beijing and the map works well, but rhe names of Chinese places show as messy code, what should I do? <img src="/upfiles/map1.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '16, 05:14</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-51467" class="comments-container">
&#10;</div>
<div id="comment-tools-51467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51467-form-container" class="comment-form-container">
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

<span id="51469"></span>

<div id="answer-container-51469" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51469-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That looks as if you are missing fonts, while not the same style the information on fonts here <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md">https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md</a> may be halpful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '16, 07:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-51469" class="comments-container">
<span id="51475"></span>
<div id="comment-51475" class="comment">
<div id="post-51475-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can I add fonts? I run the command sudo apt-get install fonts-dejavu-core fonts-droid ttf-unifont \ fonts-sipa-arundina fonts-sil-padauk fonts-khmeros \ fonts-beng-extra fonts-gargi fonts-taml-tscu fonts-tibetan-machine as the install.md said, but it doesn't work, I don't how to add the new install fonts to the stylesheet. Can you express more clearly? I am not familiar with it, thanks.</p>
</div>
<div id="comment-51475-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 09:23)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-51469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51469-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51471"></span>

<div id="answer-container-51471" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51471-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are missing fonts for chinese characters. I think that font style is <a href="https://github.com/mapbox/osm-bright">OSM Bright</a>, which had this problem for a long time. There is now a <a href="https://github.com/mapbox/osm-bright/pull/101">merged pull request</a> which fixes this problem. So if you downloaded it recently it <em>should</em> work. If not try to redownload.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '16, 08:11</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-51471" class="comments-container">
<span id="51477"></span>
<div id="comment-51477" class="comment">
<div id="post-51477-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I changed the /usr/local/etc/renderd.conf file, I replace the font_dir=/usr/share/fonts/truetype/ttf-dejavu line with font_dir=/usr/share/fonts/truetype/unifont, then the problem solved. But the pagesite you provide said that unifont does, but it also shows a character for the left-to-right mark, and hence unsuitable. And it said that I should add in the fonts that the <a href="https://github.com/gravitystorm/openstreetmap-carto/">https://github.com/gravitystorm/openstreetmap-carto/</a> project uses, but I don't konw how to add the new fonts, can you help me,thanks.</p>
</div>
<div id="comment-51477-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 10:25)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-51471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51471-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51474"></span>

<div id="answer-container-51474" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51474-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I run the command <strong>sudo apt-get install fonts-dejavu-core fonts-droid ttf-unifont \ fonts-sipa-arundina fonts-sil-padauk fonts-khmeros \ fonts-beng-extra fonts-gargi fonts-taml-tscu fonts-tibetan-machine</strong> as the install.md said in the <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md">https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md</a> .But I don't know where did the font download, and the problem do not solve. I then change the /usr/local/etc/renderd.conf file, I replace the <strong>font_dir=/usr/share/fonts/truetype/ttf-dejavu</strong> line with <strong>font_dir=/usr/share/fonts/truetype/unifont</strong>, then the problem solved, I don't if the method is correct and would not generate other problems in the future.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '16, 09:15</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-51474" class="comments-container">
&#10;</div>
<div id="comment-tools-51474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51474-form-container" class="comment-form-container">
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

