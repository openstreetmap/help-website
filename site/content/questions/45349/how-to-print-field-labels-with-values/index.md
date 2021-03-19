+++
type = "question"
title = "How to print field labels with values"
description = '''Hi, I am trying to print some fields from a capture. tshark -te -T fields -E separator=/s -E quote=n -e frame.number -e frame.time_epoch -e udp.srcport -r file  I get output which is free-form, like : 41 1305113271.649346000 2123  What I need is a name=value pair in the lines. How can I achieve the ...'''
date = "2015-08-25T15:44:00Z"
lastmod = "2015-08-29T08:20:00Z"
weight = 45349
keywords = [ "fields", "tshark" ]
aliases = [ "/questions/45349" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to print field labels with values](/questions/45349/how-to-print-field-labels-with-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45349-score" class="post-score" title="current number of votes">0</div><span id="post-45349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to print some fields from a capture.</p><pre><code>tshark -te -T fields -E separator=/s -E quote=n  -e frame.number -e frame.time_epoch -e udp.srcport -r file</code></pre><p>I get output which is free-form, like :</p><pre><code>41 1305113271.649346000 2123</code></pre><p>What I need is a name=value pair in the lines. How can I achieve the following:</p><pre><code>frame=41 time=1305113271.649346000 udp.srcport=2123 ...</code></pre><p>As you can see, in the output I want, I need the field name with every entry.</p><p>How can I achieve this?</p><p><strong>edit:</strong></p><p>The above excerpt of a highly simplified version of the fields which are needed. In reality, there are about 20 fields and many of them are specific to the messages type. So, I cannot really depend upon the order of the fields and such. If there is no way from tshark to provide it, it doesn't work for me. I need the ouput to be parseable so that I can process about 100GB of captures.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '15, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/7bf188c883a725fbcce3f1445dae3032?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prateek&#39;s gravatar image" /><p><span>Prateek</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prateek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Aug '15, 06:21</strong> </span></p></div></div><div id="comments-container-45349" class="comments-container"><span id="45507"></span><div id="comment-45507" class="comment"><div id="post-45507-score" class="comment-score"></div><div class="comment-text"><p>Based on comments so far, it is clear to me that there is no option built into tshark to do what I want. I have accepted one of the answers. However, I will implement the same logic in the python script which I have for processing those files.</p></div><div id="comment-45507-info" class="comment-info"><span class="comment-age">(29 Aug '15, 08:20)</span> <span class="comment-user userinfo">Prateek</span></div></div></div><div id="comment-tools-45349" class="comment-tools"></div><div class="clear"></div><div id="comment-45349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45354"></span>

<div id="answer-container-45354" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45354-score" class="post-score" title="current number of votes">0</div><span id="post-45354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Prateek has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about just using an awk script, assuming the columns are predictable in the output (no cases of two values in one column). Something like:</p><pre><code>tshark -T fields -E separator=/s -E quote=n  -e frame.number -e frame.time_epoch -e udp.srcport -r file | awk &#39;{ $1 = &quot;frame.number&quot; $1; $2 = &quot;time=&quot; $2; $3 = &quot;udp.srcport&quot; $3; print }&#39;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '15, 23:14</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-45354" class="comments-container"><span id="45367"></span><div id="comment-45367" class="comment"><div id="post-45367-score" class="comment-score"></div><div class="comment-text"><p>Although your answer solves the issue for simple cases, it does not solve the problem for me. There are more fields and some of them are specific to the request/response or message type. I need the output to be parseable so that I can process efficiently with python. If I have to post process with awk anyway, then I would rather do it in python itself. I wanted not to depend upon the order of fields.</p></div><div id="comment-45367-info" class="comment-info"><span class="comment-age">(26 Aug '15, 06:23)</span> <span class="comment-user userinfo">Prateek</span></div></div><span id="45381"></span><div id="comment-45381" class="comment"><div id="post-45381-score" class="comment-score"></div><div class="comment-text"><p>For fields which depend on context (like message type or request/response), the tshark output there should output null-valued cells in a case where an attribute doesn't exist in a given packet, so the column order and number should be dependably fixed either way.</p><p>If the objective is to have the attribute and value presented in each cell of output within the confines of tshark itself without post-processing, it might be possible with a Lua script though I don't believe it's possible purely within the existing tshark binary itself.</p><p>Some specific protocols such as Diameter support a "-z" option to do kind of what you're looking for, though those are protocol-specific.</p></div><div id="comment-45381-info" class="comment-info"><span class="comment-age">(26 Aug '15, 21:32)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-45354" class="comment-tools"></div><div class="clear"></div><div id="comment-45354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45477"></span>

<div id="answer-container-45477" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45477-score" class="post-score" title="current number of votes">0</div><span id="post-45477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What I need is a name=value pair in the lines. How can I achieve the following: frame=41 time=1305113271.649346000 udp.srcport=2123 ...</p></blockquote><p>Well, as tshark does not have such a funtionality, you can either pre-process the output with awk (as mentioned by <span><span>@Quadratic</span></span>), or with Perl (see below), <strong>OR</strong> do the processing in your Python code, similar to what I've done in Perl, which is totally independent on the number of fields and their order.</p><blockquote><p>tshark -nr http.pcap -T fields -e frame.number -e ip.src -e ip.dst -E separator=; -E header=y</p></blockquote><p><strong>Output:</strong></p><pre><code>frame.number;ip.src;ip.dst
1;192.168.90.55;216.34.181.60
2;192.168.90.55;216.34.181.60
3;192.168.90.55;86.58.179.120
4;192.168.90.55;23.212.211.172
5;192.168.90.55;92.122.98.7
6;192.168.90.55;92.122.98.7
7;192.168.90.55;92.122.98.7
8;192.168.90.55;216.34.181.134
9;192.168.90.55;92.122.98.7</code></pre><p><strong>Now, run that through the Perl script:</strong></p><blockquote><p>tshark -nr http.pcap -T fields -e frame.number -e ip.src -e ip.dst -E separator=; -E header=y | perl reformat.pl</p></blockquote><p><strong>Output:</strong></p><pre><code>frame.number=1 ip.src=192.168.90.55 ip.dst=216.34.181.60
frame.number=2 ip.src=192.168.90.55 ip.dst=216.34.181.60
frame.number=3 ip.src=192.168.90.55 ip.dst=86.58.179.120
frame.number=4 ip.src=192.168.90.55 ip.dst=23.212.211.172
frame.number=5 ip.src=192.168.90.55 ip.dst=92.122.98.7
frame.number=6 ip.src=192.168.90.55 ip.dst=92.122.98.7
frame.number=7 ip.src=192.168.90.55 ip.dst=92.122.98.7
frame.number=8 ip.src=192.168.90.55 ip.dst=216.34.181.134
frame.number=9 ip.src=192.168.90.55 ip.dst=92.122.98.7</code></pre><p>Of course you can also quote the field values, if there are spaces in the field values.</p><blockquote><p>tshark -nr http.pcap -T fields -e frame.number -e ip.src -e ip.dst -E separator=; -E header=y -E quote=s | perl reformat.pl</p></blockquote><pre><code>frame.number=&#39;1&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;216.34.181.60&#39;
frame.number=&#39;2&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;216.34.181.60&#39;
frame.number=&#39;3&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;86.58.179.120&#39;
frame.number=&#39;4&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;23.212.211.172&#39;
frame.number=&#39;5&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;92.122.98.7&#39;
frame.number=&#39;6&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;92.122.98.7&#39;
frame.number=&#39;7&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;92.122.98.7&#39;
frame.number=&#39;8&#39; ip.src=&#39;192.168.90.55&#39; ip.dst=&#39;216.34.181.134&#39;</code></pre><p><strong>Perl script:</strong></p><pre><code>my @header;
my $line;

BEGIN {
    chomp($line = &lt;stdin&gt;);
    @header = split(&#39;;&#39;,$line);
}

while (&lt;stdin&gt;) {
    chomp($line = $_);

    my @fields = split(&#39;;&#39;,$line);

    foreach my $i (0 .. $#fields) {
        print &quot;$header[$i]=$fields[$i] &quot;; 
    }
    print &quot;\n&quot;;
}</code></pre><p><strong>Hint</strong>: The in the code it's <strong>STDIN</strong>, however <a href="http://osqa.net/">OSQA</a> formates it to lowercase (<strong>stdin</strong>) for whatever reason. So, if you copy-paste the code, please replace <strong>stdin</strong> with <strong>STDIN</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '15, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '15, 09:36</strong> </span></p></div></div><div id="comments-container-45477" class="comments-container"></div><div id="comment-tools-45477" class="comment-tools"></div><div class="clear"></div><div id="comment-45477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

