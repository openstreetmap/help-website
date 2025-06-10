+++
type = "question"
title = "OpenSeaMap Seamark Sector Light values"
description = '''Question: I extracted the OSM XML node for a light house with sector lights to use for some graphics. However, the sector values do not make sense to me. I found the attributes mentioned on several wiki pages:  https://wiki.openstreetmap.org/wiki/Seamarks/Lights#Sectored_Light_Attributes https://wik...'''
date = "2018-09-10T09:59:00Z"
lastmod = "2018-09-10T09:59:00Z"
weight = 65846
keywords = [ "seamark", "values" ]
aliases = [ "/questions/65846" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OpenSeaMap Seamark Sector Light values](/questions/65846/openseamap-seamark-sector-light-values)

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
<span id="post-65846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65846-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Question:</strong></p>
<p>I extracted the OSM XML node for a light house with sector lights to use for some graphics. However, the sector values do not make sense to me.</p>
<p>I found the attributes mentioned on several wiki pages:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Seamarks/Lights#Sectored_Light_Attributes">https://wiki.openstreetmap.org/wiki/Seamarks/Lights#Sectored_Light_Attributes</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Seamarks/Sectored_and_Directional_Lights">https://wiki.openstreetmap.org/wiki/Seamarks/Sectored_and_Directional_Lights</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Seamarks/Seamark_Attributes">https://wiki.openstreetmap.org/wiki/Seamarks/Seamark_Attributes</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Seamarks/Radar_Beacons">https://wiki.openstreetmap.org/wiki/Seamarks/Radar_Beacons</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dlighthouse">https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dlighthouse</a></li>
</ul>
<p>but none of these seems to specify the units or interpretation of the values.</p>
<p>The first example on <a href="https://wiki.openstreetmap.org/wiki/Seamarks/Sectored_and_Directional_Lights">https://wiki.openstreetmap.org/wiki/Seamarks/Sectored_and_Directional_Lights</a> clearly shows the first sector directed to the north-east, while its values are:</p>
<pre><code>seamark:light:1:sector_end=260
seamark:light:1:sector_start=230</code></pre>
<hr />
<strong>Solution:</strong>
<p>The values are the <em>heading</em> in degrees, from a vessel. I was looking for the opposite angle...</p>
<p>Here's a Python snippet to convert the angles (you may be able to run this on an "online Python" service):</p>
<pre><code>#!python3
#coding=utf-8
&quot;&quot;&quot; Invert OSM seamark sector headings (degrees as seen from light)&quot;&quot;&quot;
import sys,re
toggle = False
with open(&quot;OSM_node.xml&quot;) as f:
  for line in f:
    if &quot;sector&quot; in line:
        # get heading angle
        mo = re.search(&quot;&#39;(\d+.\d)&#39;&quot;, line)
        heading = float( mo.groups()[0] )
        # &quot;invert&quot; angle
        angle = heading - 180
        if angle &lt; 0:
            angle = angle + 360
&#10;        # optional: flip angles &gt; 180 degrees (for SolveSpace CAD)
        if angle &gt; 180:
            angle = (angle - 360)
&#10;        # print value and add a blank line every other
        print( angle )
        if toggle:
            print()
        toggle = not toggle
&#10;# EOF</code></pre>
<hr />
PS / OT:
<blockquote>
<p>You are welcome to start submitting your question anonymously. After submiting your question, you will be redirected to the login/signup page. Your question will &gt; be saved in the current session and will be published after you login with your existing account, or signup for a new account and validate your email.</p>
</blockquote>
<p>is misleading (cannot submit anonymously) and did not work for me / question lost after registration.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-seamark" rel="tag" title="see questions tagged &#39;seamark&#39;">seamark</span> <span class="post-tag tag-link-values" rel="tag" title="see questions tagged &#39;values&#39;">values</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '18, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/adc7ce295a9d3fae8c7bacf57937a8be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whyohwhyohwhy&#39;s gravatar image" />
<p><span>whyohwhyohwhy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whyohwhyohwhy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65846" class="comments-container">
&#10;</div>
<div id="comment-tools-65846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65846-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

