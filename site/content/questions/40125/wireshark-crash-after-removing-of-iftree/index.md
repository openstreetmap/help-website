+++
type = "question"
title = "wireshark crash after removing of if(tree)"
description = '''Hi  I am developing custom dissector and i was haing issues on reassembly. with help from PASCAL i have found my reassembly is not working because of if(tree) and if i remove if(tree) i can able to open my pcap file only in debug mode (Edit -&amp;gt; preference -&amp;gt; console window = always debugging). ...'''
date = "2015-02-27T04:10:00Z"
lastmod = "2015-02-27T04:10:00Z"
weight = 40125
keywords = [ "tree", "crash", "if" ]
aliases = [ "/questions/40125" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark crash after removing of if(tree)](/questions/40125/wireshark-crash-after-removing-of-iftree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40125-score" class="post-score" title="current number of votes">0</div><span id="post-40125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am developing custom dissector and i was haing issues on reassembly.</p><p>with help from PASCAL i have found my reassembly is not working because of if(tree) and if i remove if(tree) i can able to open my pcap file only in debug mode (Edit -&gt; preference -&gt; console window = always debugging). and i can able to see my reassembly successful. but not in normal mode.</p><p>i ran MSVC debugger and found the error in trees</p><p>in dissect function under if(tree)</p><p>iam calling functions i have 8+ different functions. in debuggger i could see all my sub trees and other trees returning error</p><pre><code> ALL trees getting CXX0030 ERROR
 Mnt tree 0x00000000  null pointer.
 First child ????
 Last child ????
 Next ????
 Parent ????
 Fino ???? 
 Data ????</code></pre><p>All the trees have this same error.</p><p>my code is some thing like this</p><pre><code>         dissect function {

                                if (tree){
                                        call function1(passed tree);
                                        call function2(passed tree);
                                         }
                         }
               function1 (){
                               used tree 
                               created subtree
                               function3 (passed subtree)
                             }

         function2(){
                     used tree 
                     created subtree
                     function4 (passed subtree)
                   }
         function 4(){
                          reassembly code here..
                     }</code></pre><p>I have used wireshark build 1.11.3 and also i hae tried 1.12.3 both are getting same issue .</p><p>Some one please suggest what i can do with this ? any suggestions to oercome from this.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-if" rel="tag" title="see questions tagged &#39;if&#39;">if</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '15, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div></div><div id="comments-container-40125" class="comments-container"></div><div id="comment-tools-40125" class="comment-tools"></div><div class="clear"></div><div id="comment-40125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

