+++
type = "question"
title = "ModuleNotFoundError: No module named &#x27;osmium.replication&#x27;"
description = '''I get this module Not found error in the pyosmium-get-changes script when I execute the command  $/nominatim/build/utils/update.php --init-updates The full error message : Traceback (most recent call last):  File &quot;/usr/local/bin/pyosmium-get-changes&quot;, line 32, in &amp;lt;module&amp;gt;  from osmium.replicat...'''
date = "2023-02-22T11:54:00Z"
lastmod = "2023-02-22T11:54:00Z"
weight = 86773
keywords = [ "osmium", "pyosmium-get-changes", "pyosmium" ]
aliases = [ "/questions/86773" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ModuleNotFoundError: No module named 'osmium.replication'](/questions/86773/modulenotfounderror-no-module-named-osmiumreplication)

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
<span id="post-86773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86773-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I get this module Not found error in the pyosmium-get-changes script when I execute the command $/nominatim/build/utils/update.php --init-updates</p>
<p>The full error message : Traceback (most recent call last): File "/usr/local/bin/pyosmium-get-changes", line 32, in &lt;module&gt; from osmium.replication import server as rserv ModuleNotFoundError: No module named 'osmium.replication' Cannot execute pyosmium-get-changes. Make sure you have pyosmium installed correctly and have set up CONST_Pyosmium_Binary to point to pyosmium-get-changes. ERROR: pyosmium-get-changes not found or not usable string(44) "pyosmium-get-changes not found or not usable"</p>
<p>Content of my /nominatim/build/settings/local.php:</p>
// base URL of the replication service @define('CONST_Replication_Url', 'http://download.geofabrik.de/europe/great-britain-updates'); // How often upstream publishes diffs @define('CONST_Replication_Update_Interval', '86400'); // How long to sleep if no update found yet @define('CONST_Replication_Recheck_Interval', '900');
<p>I have installed the osmium 3.6.0 through pip, If I fire an "import osmium" on python terminal, there are no errors, but if I try executing the line "from osmium.replication import server as rserv" I get the error.</p>
<p>I need to update my database for the entire planet.</p>
<p>I've been following the steps mentioned in this article, specifically step #6 onwards <a href="https://www.linuxbabe.com/ubuntu/osm-nominatim-geocoding-server-ubuntu-20-04">https://www.linuxbabe.com/ubuntu/osm-nominatim-geocoding-server-ubuntu-20-04</a></p>
<p>Any help is appreciated, thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-pyosmium-get-changes" rel="tag" title="see questions tagged &#39;pyosmium-get-changes&#39;">pyosmium-get-changes</span> <span class="post-tag tag-link-pyosmium" rel="tag" title="see questions tagged &#39;pyosmium&#39;">pyosmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '23, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/4395c3085d362296cb36b20b4940b3e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashish&#39;s gravatar image" />
<p><span>Ashish</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashish has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '23, 12:02</strong> </span></p>
</div>
</div>
<div id="comments-container-86773" class="comments-container">
&#10;</div>
<div id="comment-tools-86773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86773-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

