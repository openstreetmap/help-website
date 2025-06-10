+++
type = "question"
title = "defaultmapping.py"
description = '''Hi I have a problem rendering my map. When I run the imposm --read command I receive the following error john@c2appsgeo02a:/data/dump$ sudo imposm --read --overwrite-cache quebec-latest.osm.pbf Traceback (most recent call last):  File &quot;/usr/bin/imposm&quot;, line 9, in &amp;lt;module&amp;gt;  load_entry_point(&#x27;i...'''
date = "2015-02-10T18:53:00Z"
lastmod = "2015-02-10T18:53:00Z"
weight = 40939
keywords = [ "defaultmapping" ]
aliases = [ "/questions/40939" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [defaultmapping.py](/questions/40939/defaultmappingpy)

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
<span id="post-40939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40939-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I have a problem rendering my map. When I run the imposm --read command I receive the following error</p>
<pre><code>john@c2appsgeo02a:/data/dump$ sudo imposm --read --overwrite-cache quebec-latest.osm.pbf
Traceback (most recent call last):
  File &quot;/usr/bin/imposm&quot;, line 9, in &lt;module&gt;
    load_entry_point(&#39;imposm==2.3.2&#39;, &#39;console_scripts&#39;, &#39;imposm&#39;)()
  File &quot;/usr/lib/python2.7/dist-packages/imposm/app.py&quot;, line 154, in main
    execfile(mapping_file, mappings)
  File &quot;/usr/lib/python2.7/dist-packages/imposm/defaultmapping.py&quot;, line 417, in &lt;module&gt;
    &#39;__any__&#39;,
TypeError: __init__() got an unexpected keyword argument &#39;with_type_field&#39;</code></pre>
<p>The error is coming from the following statements from the defaultmapping.py</p>
<pre><code>point_addresses = Points(
    name = &#39;point_addresses&#39;,
    with_type_field = False,
    fields = (
        (&#39;addr:street&#39;, String()),
        (&#39;addr:postcode&#39;, String()),
        (&#39;addr:city&#39;, String()),
        (&#39;addr:country&#39;, String()),
        (&#39;addr:housenumber&#39;, String()),
    ),
    mapping = {
        &#39;addr:housenumber&#39;: (
            &#39;__any__&#39;,
        ),
    }
)
&#10;polyline_addresses = LineStrings(
    name = &#39;polyline_addresses&#39;,
    with_type_field = False,
    fields = (
        (&#39;addr:interpolation&#39;, String()),
        ),
    mapping = {
        &#39;addr:interpolation&#39;: (
            &#39;__any__&#39;,
        ),
    }
)
&#10;polygon_addresses = Polygons(
    name = &#39;polygon_addresses&#39;,
    with_type_field = False,
    fields = (
        (&#39;addr:street&#39;, String()),
        (&#39;addr:postcode&#39;, String()),
        (&#39;addr:city&#39;, String()),
        (&#39;addr:country&#39;, String()),
        (&#39;addr:housenumber&#39;, String()),
    ),
    mapping = {
        &#39;addr:housenumber&#39;: (
            &#39;__any__&#39;,
        ),
    }
)</code></pre>
<p>Any help would be appreciated</p>
<p>Thanks in advance</p>
<p>John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-defaultmapping" rel="tag" title="see questions tagged &#39;defaultmapping&#39;">defaultmapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '15, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/5889e9a52e2b72ef52b936687a8a0c19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArmyGuy62&#39;s gravatar image" />
<p><span>ArmyGuy62</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArmyGuy62 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '15, 18:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-40939" class="comments-container">
&#10;</div>
<div id="comment-tools-40939" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40939-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

