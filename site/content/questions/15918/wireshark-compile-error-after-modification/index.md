+++
type = "question"
title = "wireshark compile error after modification"
description = '''this is the error info, i intent to put a picture here, but the system tell me &#x27;file uploading requires karma &amp;gt; 60&#x27;,i don&#x27;t know how to solve this, so i have to click all the following error info.uh, painful. make[2]:Entering directory &#x27;/home/wireshark_dissect/wireshark-1.6.4-output-formated&#x27; /us...'''
date = "2012-11-14T19:19:00Z"
lastmod = "2012-11-15T02:39:00Z"
weight = 15918
keywords = [ "compile", "error" ]
aliases = [ "/questions/15918" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark compile error after modification](/questions/15918/wireshark-compile-error-after-modification)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15918-score" class="post-score" title="current number of votes">0</div><span id="post-15918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>this is the error info, i intent to put a picture here, but the system tell me 'file uploading requires karma &gt; 60',i don't know how to solve this, so i have to click all the following error info.uh, painful.</p><pre><code>make[2]:Entering directory
&#39;/home/wireshark_dissect/wireshark-1.6.4-output-formated&#39;
/usr/bin/perl ./make-version.pl .
Version configuration file
version.conf not found. Using 
defaults. svnversion.h unchanged. cp
tools/idl2wrs.sh idl2wrs chmod +x
idl2wrs /usr/bin/perl 
./tools/make-services.pl starting to
fetch
http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt
... done fetching
http://www.iana.org/assignments/service-names-port-numbers.service-names-port-numbers.txt
http://www.iana.org/assignments/service-name-port-numbers/service-name-port-numbers.txt    doesn&#39;t have enough data make[2]: ***
[services] Error 255 make[2]: Leaving directory `home/wireshark_dissect/wireshark-1.6.4-   output-formatted`
make:*** [all] Error 2</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '12, 19:19</strong></p><img src="https://secure.gravatar.com/avatar/18b671a9df9f8c8d67a5fce658c10e81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rodman&#39;s gravatar image" /><p><span>rodman</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rodman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '12, 21:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-15918" class="comments-container"></div><div id="comment-tools-15918" class="comment-tools"></div><div class="clear"></div><div id="comment-15918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15919"></span>

<div id="answer-container-15919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15919-score" class="post-score" title="current number of votes">0</div><span id="post-15919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try to open the following link in a browser</p><blockquote><p><code>http://www.iana.org/assignments/service-name-port-numbers/service-name-port-numbers.txt</code><br />
</p></blockquote><p>The file does not exist and that's why <a href="http://make-services.pl">make-services.pl</a> reports the following error message</p><blockquote><p><a href="http://www.iana.org/assignments/service-name-port-numbers/service-name-port-numbers.txt">http://www.iana.org/assignments/service-name-port-numbers/service-name-port-numbers.txt</a> <strong>doesn't have enough data</strong></p></blockquote><p>As a <strong>quick fix</strong>, you could change the perl script <code>wireshark/tools/make-services.pl</code></p><p>from this:<br />
</p><blockquote><p><code>my $iana_port_url = "http://www.iana.org/assignments/service-name-port-numbers/service-names-port-numbers.txt";</code><br />
</p></blockquote><p>to this:</p><blockquote><p><code>my $iana_port_url = "http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt";</code><br />
</p></blockquote><p>Difference: service-name-port-numbers -&gt; service-name<strong>s</strong>-port-numbers</p><p>The better fix, would (probably) be to update your copy of the source code to the current release.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 20:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '12, 20:54</strong> </span></p></div></div><div id="comments-container-15919" class="comments-container"><span id="15920"></span><div id="comment-15920" class="comment"><div id="post-15920-score" class="comment-score"></div><div class="comment-text"><p>Sorry,Dear Kurt,i just made a mistake,the error info actually is 'fetching <a href="http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt">http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt</a> doesn't have enough data',the website can be open in my browser,but it still returns error in the compiling process.</p></div><div id="comment-15920-info" class="comment-info"><span class="comment-age">(14 Nov '12, 22:53)</span> <span class="comment-user userinfo">rodman</span></div></div><span id="15921"></span><div id="comment-15921" class="comment"><div id="post-15921-score" class="comment-score"></div><div class="comment-text"><p>O.K., then the perl script was unable to load the file (maybe due to a proxy)?</p></div><div id="comment-15921-info" class="comment-info"><span class="comment-age">(14 Nov '12, 23:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15925"></span><div id="comment-15925" class="comment"><div id="post-15925-score" class="comment-score"></div><div class="comment-text"><p>can you start the script manually and then watch the Download with Wireshark?</p><blockquote><p><code>/usr/bin/perl /home/wireshark_dissect/wireshark-1.6.4-output-formated/tools/make-version.pl</code><br />
</p></blockquote><p>Is the script able to fetch the whole (right) file?</p></div><div id="comment-15925-info" class="comment-info"><span class="comment-age">(15 Nov '12, 02:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15919" class="comment-tools"></div><div class="clear"></div><div id="comment-15919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

