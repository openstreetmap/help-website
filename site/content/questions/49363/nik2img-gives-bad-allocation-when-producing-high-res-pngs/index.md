+++
type = "question"
title = "Nik2img gives &quot;bad allocation&quot; when producing high res pngs"
description = '''Hello Community, I am having problems using Nik2Img. We want to produce high resolution geo-referenced PNGs, which works pretty well, until a certain Bounding Box size or &quot;zoom level&quot; is reached. Probably at resulting pngs bigger  than 50 Megabytes.  Output: D:&#92;osm&#92;mapnik&#92;nik2img&amp;gt;D:&#92;osm&#92;mapnik&#92;ni...'''
date = "2016-04-22T14:05:00Z"
lastmod = "2016-04-26T09:02:00Z"
weight = 49363
keywords = [ "mapnik", "nik2img" ]
aliases = [ "/questions/49363" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nik2img gives "bad allocation" when producing high res pngs](/questions/49363/nik2img-gives-bad-allocation-when-producing-high-res-pngs)

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
<span id="post-49363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49363-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Community, I am having problems using Nik2Img. We want to produce high resolution geo-referenced PNGs, which works pretty well, until a certain Bounding Box size or "zoom level" is reached. Probably at resulting pngs bigger than 50 Megabytes.</p>
<p>Output: D:\osm\mapnik\nik2img&gt;D:\osm\mapnik\nik2img\nik2img.py D:\osm\mapnik\osm.xml D:\ Tiles\Mstb_2500.png --srs 21781 --bbox 8.15516 47.48854 8.30227 47.55949 --world -file wld --dimensions 17600 12800 Traceback (most recent call last): File "D:\osm\mapnik\nik2img\nik2img.py", line 238, in &lt;module&gt; main() File "D:\osm\mapnik\nik2img\nik2img.py", line 232, in main nik_map.open() File "D:\osm\mapnik\nik2img\mapnik_utils\composer.py", line 218, in open self.render() File "D:\osm\mapnik\nik2img\mapnik_utils\composer.py", line 327, in render renderer = super(ComposeDebug,self).render() File "D:\osm\mapnik\nik2img\mapnik_utils\composer.py", line 210, in render renderer.render_file() File "D:\osm\mapnik\nik2img\mapnik_utils\renderer.py", line 247, in render_fil e self.local_render_wrapper(self.m, self.image, self.format) File "D:\osm\mapnik\nik2img\mapnik_utils\renderer.py", line 131, in local_rend er_wrapper self.render_to_file(<em>args) File "D:\osm\mapnik\nik2img\mapnik_utils\renderer.py", line 199, in render_to_ file mapnik.render_to_file(</em>args) RuntimeError: bad allocation</p>
<p>Any idea, how we can resolve this issue? We wanted to go this route instead of "generate_tiles.py" to later let our GIS-frontend tileseed the big rasters...</p>
<p>Thx for any advice.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-nik2img" rel="tag" title="see questions tagged &#39;nik2img&#39;">nik2img</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '16, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/1d567ce59a77746f6234fe343a508488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="do4sch&#39;s gravatar image" />
<p><span>do4sch</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="do4sch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49363" class="comments-container">
<span id="49364"></span>
<div id="comment-49364" class="comment">
<div id="post-49364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>we figured, that at about 12000x12000 pixels (depending on bounding box size) it throws this error. Anyone knows, if theres a "pixel-size-limit" with Nik2Img? We would need to create very large rasters to cover big scales...</p>
</div>
<div id="comment-49364-info" class="comment-info">
<span class="comment-age">(22 Apr '16, 14:32)</span> <span class="comment-user userinfo">do4sch</span>
</div>
</div>
<span id="49365"></span>
<div id="comment-49365" class="comment">
<div id="post-49365-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This really looks like a software issue which is best raised on the relevant issue tracker.</p>
</div>
<div id="comment-49365-info" class="comment-info">
<span class="comment-age">(22 Apr '16, 16:01)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="49381"></span>
<div id="comment-49381" class="comment">
<div id="post-49381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could try if nik4 gives you the same problems - nik4 can do everything nik2img can do but the invocation is a bit different. Having said that, generating giant GeoTIFFs and then splitting them in tiles seems like an unnecessary complication to me; being able to render small tiles is something that makes things easier, not harder...</p>
</div>
<div id="comment-49381-info" class="comment-info">
<span class="comment-age">(23 Apr '16, 19:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="49427"></span>
<div id="comment-49427" class="comment">
<div id="post-49427-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik for your hint to Nik4... I was able to render Tiles of big bounding boxes with Nik4 successfully, even in a "custom" projection. Why does altering the projection in the mapnik-xml has no influence? Do scripts like Nik2Img and Nik4 override the projection set in osm.xml?</p>
</div>
<div id="comment-49427-info" class="comment-info">
<span class="comment-age">(26 Apr '16, 09:02)</span> <span class="comment-user userinfo">do4sch</span>
</div>
</div>
</div>
<div id="comment-tools-49363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49363-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

