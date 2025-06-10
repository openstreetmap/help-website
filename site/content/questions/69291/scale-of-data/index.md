+++
type = "question"
title = "Scale of data"
description = '''Background: I often need to produce thematic cartography for different applications (Environmental Impact Assessment is one of them). By law (Portugal), when you create thematic cartography for any official use, you need to specify the origin of the different data used, including scale/resolution in...'''
date = "2019-05-23T22:19:00Z"
lastmod = "2019-05-25T18:42:00Z"
weight = 69291
keywords = [ "data" ]
aliases = [ "/questions/69291" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Scale of data](/questions/69291/scale-of-data)

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
<span id="post-69291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69291-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Background:</strong> I often need to produce thematic cartography for different applications (Environmental Impact Assessment is one of them). By law (Portugal), when you create thematic cartography for any official use, you need to specify the origin of the different data used, including scale/resolution information. I often need to mix different information, from different origins, with different scales (from OSM data to climatic data at 1:1.000.000...).</p>
<p>Vector data do have a 'base scale' or at least a 'positional error', that should always be considered when you are representing the data. It might be - or not - relevant to the use you are considering.</p>
<p>If the data was captured by a GPS unit, for instance, then you might have to consider a positional error corresponding to the positional error of the GPS reading. As an example, I have an old Garmin GPSmap 60C unit, which has a maximum accuracy of 4 meters, but which normally works with values of 6 to 9 meters, depending on the number of satellites available, their position on the sky, the degree of tree coverage, the presence of high buildings or structures...).</p>
<p>If the data comes from vectorized paper maps, then you need to consider the scale of the original map, which has its own positional error. In the Portuguese case, which is the one I'm familiar with, for 1:25.000 maps, the positional error is 12.5 meters, which corresponds to 0.5 mm on the paper. But if you have data digitized from a 1:1.000.000 map, then the positional error is much higher (500 meters, if we assume the same 0.5 mm on paper).</p>
<p>If you create cartography to be printed and used on the field, based on different data, it is fundamental to be conscious of their different origins and scale / positional error, and you should clearly state that information on the map regarding the base information. That is why I have been looking for the best way to describe OSM data scale / positional error.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '19, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/e1a5f7fd1a95f194f2b3c8d92781f327?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luis%20Valen%C3%A7a%20Pinto&#39;s gravatar image" />
<p><span>Luis Valença...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luis Valença Pinto has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>25 May '19, 18:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-69291" class="comments-container">
<span id="69292"></span>
<div id="comment-69292" class="comment">
<div id="post-69292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you need data with that degree of uniformity and certainty, OSM is not the data source for you. Data comes from hundreds of different sources and is digitised to thousands of different standards and abilities.</p>
<p>Think of it as a charitable endeavour keeping legacy data suppliers in business.</p>
</div>
<div id="comment-69292-info" class="comment-info">
<span class="comment-age">(24 May '19, 11:21)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="69299"></span>
<div id="comment-69299" class="comment">
<div id="post-69299-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please create questions when asking questions and don't use answers.</p>
</div>
<div id="comment-69299-info" class="comment-info">
<span class="comment-age">(25 May '19, 18:42)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69291-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

