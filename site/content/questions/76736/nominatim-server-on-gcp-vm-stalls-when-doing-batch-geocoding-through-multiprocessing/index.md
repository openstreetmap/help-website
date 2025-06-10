+++
type = "question"
title = "Nominatim Server on GCP VM Stalls When Doing Batch Geocoding Through Multiprocessing"
description = '''Hello all, I really need help on this front! I&#x27;ve set up a Nominatim Server on GCP&#x27;s Compute Engine. It works ok enough, but now I have 100 million unique addresses that I need to forward-geocode through my service, and I&#x27;m trying to use multiprocessing to speed things up - even 100 addresses proces...'''
date = "2020-09-20T23:58:00Z"
lastmod = "2020-09-21T17:55:00Z"
weight = 76736
keywords = [ "python", "parallelization", "nominatim", "multiprocessing" ]
aliases = [ "/questions/76736" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim Server on GCP VM Stalls When Doing Batch Geocoding Through Multiprocessing](/questions/76736/nominatim-server-on-gcp-vm-stalls-when-doing-batch-geocoding-through-multiprocessing)

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
<span id="post-76736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76736-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I really need help on this front! I've set up a Nominatim Server on GCP's Compute Engine. It works ok enough, but now I have 100 million unique addresses that I need to forward-geocode through my service, and I'm trying to use multiprocessing to speed things up - even 100 addresses processed simultaneously stalls the service. My VM has 128 GB of RAM &amp; 24 CPUs. I followed the configuration recommendations from the installation guide. Does anyone have any best practices for setting up the service for handling HUGE bulk-loads? Would switching from apache to nginx help?</p>
<p>Reproduceable Code Example in Python:</p>
<pre><code>from joblib import Parallel, delayed
from multiprocessing import cpu_count
from geopy.geocoders import Nominatim
from collections import defaultdict
&#10;def geopy_parse(address_str):
    &quot;&quot;&quot;
    Use Custom Nominatim Server to Extract 
    Country, Locality and Region from Unstructured Address
    &quot;&quot;&quot;
    osm = Nominatim(domain=&quot;&lt;url&gt;&quot;, scheme=&quot;http&quot;, timeout=10000)
    result = osm.geocode(address_str, language=&#39;en&#39;, addressdetails=True)
    if result is not None:
        return defaultdict(lambda: None, result.raw[&#39;address&#39;])
    else:
        return None
&#10;addresses = [&#39;Vancouver BC Canada&#39;]*100
Parallel(n_jobs=cpu_count())(delayed(geopy_parse)(a) for a in addresses)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-parallelization" rel="tag" title="see questions tagged &#39;parallelization&#39;">parallelization</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-multiprocessing" rel="tag" title="see questions tagged &#39;multiprocessing&#39;">multiprocessing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '20, 23:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f8dd6d1f5bf765fbbb3001eb3bdf3f60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rirhun&#39;s gravatar image" />
<p><span>rirhun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rirhun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '20, 23:59</strong> </span></p>
</div>
</div>
<div id="comments-container-76736" class="comments-container">
&#10;</div>
<div id="comment-tools-76736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76736-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="76742"></span>

<div id="answer-container-76742" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76742-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rirhun has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For installations with a high load, you should switch your server at least to <a href="https://php-fpm.org/">php-fpm</a>. In my experience it is also worth switching to nginx, as it is much better in coping with many parallel requests. Your system setup should be able to manage 600 request/s. (It depends on how the VM is set up, in particular, how fast is access to the disks.)</p>
<p>On a general note: it is not really worth increasing the number of parallel requests infinitely. Your server has a fixed number of CPUs and that limits the number of parallel work you can do. Too many parallel request and they get in each other's way, which actually slows you down. In your case I would expect that beyond 50 parallel requests you won't see much increase in throughput.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '20, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-76742" class="comments-container">
<span id="76748"></span>
<div id="comment-76748" class="comment">
<div id="post-76748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the insightful response - I'm using an SSD so access to disk should be relatively fast I believe. I tried looking into nginx and it wasn't working - the server kept complaining "file not found" w/ regards to the php-fpm.socket even though the path to the socket was correct.</p>
</div>
<div id="comment-76748-info" class="comment-info">
<span class="comment-age">(21 Sep '20, 17:55)</span> <span class="comment-user userinfo">rirhun</span>
</div>
</div>
</div>
<div id="comment-tools-76742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76742-form-container" class="comment-form-container">
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

