+++
type = "question"
title = "Argument List too Long"
description = '''Hello, I&#x27;ve written this simple script for tshark. What it does is extract all of the TCP connections that contain a SYN packet within the capture. #!/bin/bash  file=$1 outfile=$2  string=&quot;&quot; counter=0  for src in `tshark -r $file -R &quot;tcp.flags.syn == 1&quot; -T fields -e ip.src -e ip.dst -e tcp.srcport -...'''
date = "2010-09-22T11:10:00Z"
lastmod = "2010-09-22T11:24:00Z"
weight = 262
keywords = [ "tshark" ]
aliases = [ "/questions/262" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Argument List too Long](/questions/262/argument-list-too-long)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-262-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I've written this simple script for tshark. What it does is extract all of the TCP <em>connections</em> that contain a SYN packet within the capture.</p><pre><code>#!/bin/bash

file=$1
outfile=$2

string=&quot;&quot;
counter=0

for src in `tshark -r $file -R &quot;tcp.flags.syn == 1&quot; -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport | cut -d &#39; &#39; -f1-4`
do
    if [ $counter == 0 ]; then
        string=$string&quot;(ip.src == $src &amp;&amp; &quot;
    elif [ $counter == 1 ]; then
        string=$string&quot;ip.dst == $src &amp;&amp; &quot;
    elif [ $counter == 2 ]; then
        string=$string&quot;tcp.srcport == $src &amp;&amp; &quot;
    else
        string=$string&quot;tcp.dstport == $src) || &quot; 
    fi

    if [ $counter == 3 ]; then
        let counter=0
    else
        let counter=$counter+1
    fi 
done

string=${string%????}

tshark -r $file -R &quot;$string&quot; -w &quot;$outfile&quot;</code></pre><p>My problem is, for large .pcap files, I get an "argument list too long" error when executing the final tshark command. I assume my filter grows too large.</p><p>Is there any scripting wizardry that would allow me to duplicate my expected results without getting an "argument list too long" error?</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '10, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/832728debd1b180125e7979571c329f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmkastn&#39;s gravatar image" /><p>cmkastn<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmkastn has no accepted answers">0%</span></p></div></div><div id="comments-container-262" class="comments-container"></div><div id="comment-tools-262" class="comment-tools"></div><div class="clear"></div><div id="comment-262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="264"></span>

<div id="answer-container-264" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-264-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could make the filter smaller by using the "tcp.stream==&lt;x&gt;" filter instead of two ip/ip/port/port filters per connection. This would change your script into:</p><pre><code>#!/bin/bash

file=$1
outfile=$2

filter=&quot;&quot;

for stream in `tshark -r $file -R &quot;tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack==0&quot; -T fields -e tcp.stream`
do
    filter=$filter&quot;tcp.stream==$stream||&quot; 
done

string=${string%??}

tshark -r $file -w &quot;$outfile&quot; $filter</code></pre><p>Of course that only helps to a certain amount. If you really want to be safe in all situations, you can loop through all the tcp sessions and filter them out individually into new files and then merge them all together with mergecap afterwards. But that's uhmm... well, nit very efficient ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '10, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-264" class="comments-container"></div><div id="comment-tools-264" class="comment-tools"></div><div class="clear"></div><div id="comment-264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

